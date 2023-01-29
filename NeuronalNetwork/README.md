### Neuronal Network

Here are the models we pre-trained.
  - best.pt: best model after entire training and the model we used in our application
  - secondBest.pt: second best model after entire training
  - longestTrained.pt: longest trained model
 
To further train the model, the paths to the split datasets must first be specified in the coco.yaml file. The path must lead to the location of the data set folder and the text files for splitting the data into validation, test and training data. In this case it would be a path to the Dataset folder. In addition, the number of classes and the names of all classes in the file must be entered. All class names must also be enumerated in the classes.names file. 
The files coco.yaml, classes.names, and the desired pre-trained model weights, e.g. best.pt, must now be copied into the cloned yolov5 folder. 
Here is also the Python script train.py, with which the model can be trained further. Thereby, various parameters can be personalized. For example, if you want to train the model "best.pt" for 50 epochs on the data set according to "coco.yaml" with a batch size of 32, you call the script as follows: 
  python val.py --weights best.pt --data './coco.yaml'.
