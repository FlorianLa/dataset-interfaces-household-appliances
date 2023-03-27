## Example Application
The application requires a computer with a camera and Python 3.7. Further, you need to download the Yolov5 code (https://github.com/ultralytics/yolov5). We used version 6.1 and provide a backup of this version in this repository.

Then, replace the detect.py file with our file and copy constrGlob.py, constrKnob.py, constrPush.py, constrSlider.py, and constrToggle.py, into the utils folder of the yolov5 directory. 

In these five files, you can adjust the augmentations of the different labels manually. 

The individual files are:
  - constrGlob.py: Creates different global highlights.
    - constrKnob.py: Creates different visualizations for *Knobs*.
    - constrPush.py: Creates different visualizations for *Pushbuttons*.
    - constrSlider.py: Creates different visualizations for *Sliders*.
    - constrToggle.py: Creates different visualizations for *Toggles*. 
  - detect.py: Calls the required construction scripts with the specified parameters.
