# Availability of DUV images
Deep UltraViolet Breast Cancer images are not available to the public, since it is a private dataset shared to me by Tongtong Lu. 
If you are interested in attaining the DUV images that was used in this research, contact him or the Marquette Biophotonics Lab for permission to use the images. 
https://mcw.marquette.edu/biomedical-engineering/biophotonics-lab/graduate-students.php

# Abstract
The purpose of this research is to aid medical professionals with diagnosing cancer in breast tissue. It utilizes Deep Ultraviolet (DUV) fluorescence images of breast cancer tissue for the deep learning approach. This readme will briefly talk about the research by first introducing possible solutions to current problems with breast-conserving surgery (BCS) and Hematoxylin and eosin stain (H&E) images. In the attached poster, the methodology of the deep learning approach will be briefly described with a patch-based transfer learning approach. Afterwards, experimental results will be shown with a quantitative evaluation of the method, and qualitative evaluation of the DUV images for intra-operative breast cancer margin assessment.

# Brief Intro on Summer Undergraduate Research Fellowship
Breast-conserving surgery (BCS) aims to remove tumor tissue and preserve normal tissue as much as possible. Patients face cancer recurrence if the cancer cells are not removed entirely and remain on the tissue. Also, they may need to have additional surgery to removed remaining cancer cells. A post-operative procedure is done if positive margin for cancer is detected in the tissue. Standard deep learning approaches are limited by small datasets that comprise of only Whole Slide Images (WSI). By only using the WSI, the deep learning models have a blackbox of information that pathologists cannot directly see or understand. In other words, they do not understand which features that the model focuses on for classification of cancer. One way to resolve these issues is to have a patch-based approach that will split a single WSI into much smaller segments(400x400). With this, it will help to localize tumors with a grid system, which provides surgeon possible dissection locations. Alongside with this, an extreme gradient boosting tree, or XGBoost can be utilized for this limited training data, while preventing overfitting. Previously, H&E staining has been used for breast cancer, however it may not show all the important cancer risk features. DUV images can tackle this issue by increasing the contrast of the features on the image.

[Poster.pdf](https://github.com/dominusoctane/Breast-Cancer-Research/files/7566537/Poster.pdf)

# WORK IN PROGRESS:
-Transfer Learning approach with H&E images applied onto DUV WSI
-Use GradCam to get the weight map from the DUV WSI
-Visualize the activation map
-Test with DUV WSI patch images
