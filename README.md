## A Dataset and Machine Learning Approach to Classify and Augment Interface Elements of Household Appliances to Support People with Visual Impairment
Our work is published under GNU GPLv3. However, other licenses may apply for some files, e.g., backups of the used repositories or the published paper. This repository complements a publication in the ACM digital library (https://doi.org/10.1145/3581641.3584038). The publication is contained in this repository as a PDF file or can be accessed on the ACM library as PDF or HTML free of charge.

### General Information and Disclaimer
This repository (or rather the releases of this repository) is mirrored on Zenodo.org (https://doi.org/10.5281/zenodo.7586106).

The dataset itself can be found in the latest release (https://github.com/FlorianLa/dataset-interfaces-household-appliances/releases/tag/v0.91). 

Further, this repository contains an example application on augmenting interfaces, instructions on creating and labeling more images, and a trained neuronal network, as detailed below.

### Dataset
The dataset consists of 13702 images with 75,551 manually labeled interface elements. The elements are differentiated into the five categories *Knob*, *Slider*, *Toggle*, *PushButton*, and *Touchbutton*. More details regarding the images, i.e., light situation, type of household appliance, model (if available), and other data, are listed in a separate File.

### Example Application
The example application demonstrates how a trained neuronal network could be used to visually augment a camera stream. Prerequisites are a computer with a camera and Python version 3.7 installed.

The presented augmentations can be customized.

### Extending the Dataset
To extend the dataset, you need to collect images or videos and use our python script to extract images from them. We added instructions and example texts for the grant of rights of use.

Afterwards, you need to label the images with LabelImg.
Feel free to drop us a message or pull request if you want us to include your images in the dataset.

### Neuronal Network
We used a Yolov5s Model and the code from their GitHub (https://github.com/ultralytics/yolov5) to train a neuronal network on our dataset. We provide the model for download.