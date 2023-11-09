from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications import resnet50
from tensorflow.keras import Model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, save_img
import time
import os
import numpy as np

class ResNetClass:
    
    '''Class for storing base ResNet model and weights'''
    def __init__(self):
        self.base_model = ResNet50(weights='imagenet')
        self.layer_models = dict()
    
    def get_resnet_model(self, layer_name='avg_pool'):
        '''Returns resnet model with desired last layer.'''
        try:
            model = self.layer_models[layer_name]
            print('Model ({}) found.'.format(layer_name))
            return model
        except KeyError:
            print('Model ({}) not found. Adding model to model dictionary.'.format(layer_name))
            self.layer_models[layer_name] = Model(inputs=self.base_model.input, outputs=self.base_model.get_layer(layer_name).output)
            return self.layer_models[layer_name]
             
    def save_resnet_predictions(self, df, save_folder, model, verbose=0,mode=0):
        '''Saves resnet predictions for each image as .npy'''
        i = 0
        if verbose: start = time.time()
        for _, row in df.iterrows():
            if i % 1000 == 0 and verbose: print(i, time.time()-start)
            
            if mode==0:
                save_name = str(row['filename']) + '_' + str(row['rotation']) + '_' + str(int(row['flip'])) + '.npy'
            else:
                save_name = str(row['filename']) + '.npy'
            
            save_path = os.path.join(save_folder, save_name)
            if not os.path.isfile(save_path):
                # load image
                img = load_img(row['fullpath'], target_size=(224, 224, 3)) # PIL.Image.Image
                img_array = img_to_array(img)

                # rotation and flips
                if mode ==0:
                    img_array = np.rot90(img_array, row['rotation'])
                    if row['flip']:
                        img_array = np.flipud(img_array)

                # get features
                x = np.expand_dims(img_array, axis=0) # add 1 to front of shape
                x = resnet50.preprocess_input(x)
                pred = model.predict(x)

                # save features for later
                np.save(save_path, pred)
            i += 1
