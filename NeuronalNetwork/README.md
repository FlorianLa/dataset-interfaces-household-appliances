### Neuronal Network

Here, we provide three different pre-trained models:
  - best.pt: This is the best model after the entire training and the model we used in our application.
  - secondBest.pt: Second best model.
  - longestTrained.pt: This is the model with the longest training duration.

If you would like to continue training the model on our dataset you have to:
 - Download the Yolov5 code (https://github.com/ultralytics/yolov5). We used version 6.1 and provide a backup of this version in this repository.
 - Specify the paths to the split dataset in coco.yaml. The path must lead to the location of the dataset and the text files for splitting the data into validation, test, and training sets (see dataset).
 - Enter the number of classes and their names. Also, enumerate the class names in the classes.names file. 
 - Copy the files coco.yaml, classes.names, and the desired pre-trained model weights, e.g., best.pt, into the yolov5 folder.
 - Modify the script train.py and adjust all parameters to your needs.
 - To train the model "best.pt" for 50 epochs on the data set according to "coco.yaml" with a batch size of 32, you call the command "python train.py --batch 32 --epochs    50 --weights best.pt --data './coco.yaml'".
