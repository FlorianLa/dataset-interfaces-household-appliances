## Example Application

To test the application you need a computer with camera and Python version 3.7. 

For this, the Git repository of yolov5 must first be cloned (https://github.com/ultralytics/yolov5 - tested with version 6.1).
The detect.py file must be replaced with the file presented here. In addition, the five python files, constrGlob.py, constrKnob.py, constrPush.py, constrSlider.py, and constrToggle.py, in the utlis folder must be copied to the utils folder of the yolov5 directory. 

Through these files the augmentation of the labels can be adjusted manually:
  - constrGlob.py: creates different global highlights
	- constrKnob.py: creates different visualizations for knobs
	- constrPush.py: creates different visualizations for pushbuttons
	- constrSlider.py: creates different visualizations for sliders
	- constrToggle.py: creates different visualizations for toggles 
  - detect.py: calls the required construction scripts with the required parameters
