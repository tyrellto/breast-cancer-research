# Breast Cancer Research with ML/AI Applications
---
**Table of Contents**
- [Abstract](#abstract)
- [Dataset](#dataset)
- [Method](#method)
- [Quantitative Results](#quantitative-results)
- [Qualitative Results](#Qualitative-results)
- [Conclusion](#conclusion)

  
<h2>Publications</h2>
<ul>
    <li>
        <p>
            <b>Deep learning classification of deep ultraviolet fluorescence images toward intra-operative margin assessment in breast cancer</b><br>
            <i>Frontiers for Oncology 2023</i>, 6/16/2023<br>
            <a href="https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2023.1179025/full" target="_blank">Read the full article</a>
        </p>
    </li>
    <li>
        <p>
            <b>Deep Learning for Breast Cancer Classification of Deep Ultraviolet Fluorescence Images toward Intra-Operative Margin Assessment</b><br>
            <i>2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)</i>, 8/22/2022, Oral presentation<br>
            <a href="https://ieeexplore.ieee.org/document/9871819" target="_blank">Conference proceedings</a>
        </p>
    </li>
</ul>

## Abstract
The purpose of this research is to aid medical professionals with diagnosing cancer in breast tissue. It utilizes Deep Ultraviolet (DUV) fluorescence images of breast cancer tissue for the deep learning approach. The methodology of the deep learning approach will be briefly described with a patch-based transfer learning approach. Afterwards, experimental results will be shown with a quantitative evaluation of the method, and qualitative evaluation of the DUV images for intra-operative breast cancer margin assessment.

## Dataset
The dataset comprises DUV images from 60 samples, split between 24 normal/benign and 36 malignant. These images are obtained using a custom DUV-FSM system with 285 nm ultraviolet excitation. Staining with propidium iodide and eosin Y enhances the fluorescence contrast, producing high-resolution images. The dataset, divided into 34468 patches, provides a detailed representation of the tissue characteristics necessary for training our deep learning models.

These images are not available to the public, since it is a private dataset shared with me by the Medical College of Wisconsin's tissue bank. If you are interested in attaining the DUV images that were used in this research, contact Dr. Bing Yu for permission to use the images. 
[Dr. Bing Yu's Profile](https://mcw.marquette.edu/biomedical-engineering/directory/bing-yu.php)

<p align="center">
  <img src="https://github.com/tyrellto/breast-cancer-research/assets/61175343/fc679867-3261-487e-a0e7-36080db86bed" width="800" alt="Cancer Example"/>
</p>

## Method
The method employed in this research involves a multi-step process tailored to handle the intricacies of DUV images for breast cancer detection:

<p align="center">
  <img src="https://github.com/tyrellto/breast-cancer-research/assets/61175343/0e63d83f-b9d2-455f-b798-38ae4ce65a82" width="800" alt="Process Diagram"/>
</p>

1. **Patch Extraction**: We start by dividing each DUV whole-slide image (WSI) into a series of non-overlapping patches. Each patch is analyzed for its content, ensuring a significant presence of tissue by checking the foreground pixel intensity. Can be replicated in [foreground_and_patch_extraction.ipynb](https://github.com/tyrellto/breast-cancer-research/blob/main/foreground_and_patch_extraction.ipynb)

2. **Preprocessing and Augmentation**: To address variances in dimensions across DUV WSIs, we resize images to standardized dimensions, allowing for consistent patch extraction. Part of [foreground_and_patch_extraction.ipynb](https://github.com/tyrellto/breast-cancer-research/blob/main/foreground_and_patch_extraction.ipynb)

3. **Feature Map Generation**: Using a pre-trained ResNet50, we extract feature maps for each patch. These feature maps serve as inputs to an XGBoost classifier that predicts binary outcomes for each patch, identifying regions of interest (ROIs) within the DUV WSIs. Part of [feature_extraction.ipynb](https://github.com/tyrellto/breast-cancer-research/blob/main/feature_extraction.ipynb)

4. **Explainability with Grad-CAM++**: Grad-CAM++ on a pre-trained DenseNet169 model calculates the regional importance map for the DUV WSI with the hypothesis that salient features will be captured. Part of [model_approach.ipynb](https://github.com/tyrellto/breast-cancer-research/blob/main/model_approach.ipynb), where it combines the features and images used in the **Patch Extraction**, **Preprocessing and Augmentation**, and **Feature Map Generation**

5. **Decision Fusion**: Finally, we aggregate the patch-level predictions and their associated regional importance maps to assign a comprehensive classification label to each WSI. This fusion approach ensures that our model's predictions are not only accurate but also interpretable and clinically relevant. This part only contains one hyperparameter, which is the ratio of the cancer region's size to the foreground's. Part of [model_approach.ipynb](https://github.com/tyrellto/breast-cancer-research/blob/main/model_approach.ipynb), where it combines the features and images used in the **Patch Extraction**, **Preprocessing and Augmentation**, **Feature Map Generation**, and **Explainability with Grad-CAM++**.

## Quantitative Results
Here are some figures to show the metrics of the approach. (1) in the table is a barebone ResNet50 approach, (2) is patch-level classification with majority voting, while (3) is my proposed method:

<p align="center">
  <img src="https://github.com/tyrellto/breast-cancer-research/assets/61175343/207d77a5-6c2f-4b53-9c3a-26b7f1dfb63b" width="800" alt="Accuracy Results Diagram"/>
</p>

This is a confusion matrix to show which cases for cancer and benign/normal were correctly classified and misclassified.

<p align="center">
  <img src="https://github.com/tyrellto/breast-cancer-research/assets/61175343/82ab0955-f901-4987-ae88-3f7f7feb7236" width="400" alt="Matrix Results Diagram"/>
</p>

## Qualitative Results
Here is a diagram showing some visual examples with the corresponding H&E and DUV images with overlays:

<p align="center">
  <img src="https://github.com/tyrellto/breast-cancer-research/assets/61175343/37b81291-8639-416c-a89b-7787c03355f0" width="800" alt="Image Results Diagram"/>
</p>

## Conclusion
The study successfully demonstrates the application of deep learning to DUV WSI images for breast cancer margin assessment, achieving 95.0% classification accuracy. This showcases the potential for real-time surgical guidance and the method's adaptability for various cancer types. However, limitations such as dataset size and generalizability call for further research to optimize and validate the approach for clinical use.
