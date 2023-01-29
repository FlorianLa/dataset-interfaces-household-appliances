## A Dataset and Machine Learning Approach to Classify and Augment Interface Elements of Household Appliances to Support People with Visual Impairment
Our work is published under GNU GPLv3. However, for some files, e.g., backups of the used repositories or the published paper, other licenses may apply.
The ACM Link, DOI and other infomation will be added here, after the paper is published.

### General information and Disclaimer
This repository (or rather the releases of this repository) are mirrored on Zenodo.org. (link will be added)

The Dataset itself can be found in the latest release (link will be added) 

Further, this repository contains an example application, instructions on how to create and label more images, and a trained neuronal network as detailed below.

### Dataset
The dataset consists of 13 with 75,551 manually labled interface elements. The elements are differentiated into the five categories *Knob*, *Slider*, *Toggle*, *PushButton*, and *Touchbutton*. More details regarding the images, i.e., light situation, type of the household appliance, model (if availiable), and other data is listed in a separate File.

### Example Application
The example application demonstrates how a trained neuronal network could be used to visually augment a camera stream. Prerequisites are a computer with a camera and Python version 3.7 installed.

The presented augmentations can be customized.

### Extending the Dataset
To extend the dataset you need to collect videos and use our python script to extract images, or collect images. We added instructions and example texts for the grant of rights of use.

Afterwords, you need to lable the images with LabelImg.
Fell free to drop us a message or pull request if you want us to include your images in the dataset.

### Neuronal Network
We used a Yolov5s Model and the code from their github (https://github.com/ultralytics/yolov5) to train a neuronal network on our dataset. We provide the model for download.