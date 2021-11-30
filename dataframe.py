import pandas as pd
import numpy as np
import os

#I AM ABLE TO LOGIN!!!! MUHAAAAAAAHA

def make_breakhis_df(bh_folder):
    '''makes dataframe for breakhis dataset'''    
    dflist = []
    for root, dirs, files in os.walk(bh_folder):
        for name in files:
            relpath = os.path.relpath(root, bh_folder)
            ext = os.path.splitext(name)[-1]

            # get info from filename
            name_ = name.replace("-", "_")
            name_ = name_.replace(".", "_") 
            if ext == '.png':
                try:
                    biopsy_procedure, tumor_class, tumor_type, year, slide_id, magnification, seq, ext = name_.split('_')
                    fullpath = os.path.join(root, name)
                    row = {'relpath':relpath, 'filename':name, 'biopsy_procedure':biopsy_procedure, 'tumor_class':tumor_class,
                           'tumor_type':tumor_type, 'year':year, 'slide_id':slide_id, 'magnification':magnification, 'seq':seq, 'fullpath':fullpath}
                    dflist.append(row)
                except:
                    pass
    df = pd.DataFrame(dflist)
    df['year'] = df['year'].astype(int)
    df['magnification'] = df['magnification'].astype(int)
    df['seq'] = df['seq'].astype(int)
    #df['year'] = pd.to_numeric(df['year'])
    #df['magnification'] = pd.to_numeric(df['magnification'])
    #df['seq'] = pd.to_numeric(df['seq'])
    return df


def add_rotations_to_df(df, num_rotations):
    '''add rotation column to dataframe
    adds num_rotations rows for each original row
    each new row has value from 0 to (num_rotatoins - 1)
    '''
    dflist = []
    for i, row in df.iterrows():
        for j in range(num_rotations):
            row_dict = row.to_dict()
            row_dict['rotation'] = j
            dflist.append(row_dict)
    return pd.DataFrame(dflist)


def add_flips_to_df(df):
    '''add flip column to dataframe
    adds 2 rows for each original row
    each new row has true or false value for flipping or not
    '''
    dflist = []
    for i, row in df.iterrows():
        for j in range(2):
            row_dict = row.to_dict()
            row_dict['flip'] = j
            dflist.append(row_dict)
    df_flip = pd.DataFrame(dflist)
    df_flip['flip'] = df_flip['flip'].astype(bool)
    return df_flip


def add_rotations_and_flips_to_df(df, num_rotations):
    '''adds both rotation and flip columns'''
    df_rot = add_rotations_to_df(df, num_rotations)
    return add_flips_to_df(df_rot)


def add_features_to_df(df, save_folder):
    """add features to dataframe from saved features (.npy)"""
    df_feat = df
    features = []
    for i, row in df_feat.iterrows():
        save_name = row['filename'] + '_' + str(row['rotation']) + '_' + str(int(row['flip'])) + '.npy'
        save_path = os.path.join(save_folder, save_name)
        feature = np.load(save_path)
        features.append(feature)
    df_feat['features'] = [np.squeeze(feature) for feature in features]
    return df_feat