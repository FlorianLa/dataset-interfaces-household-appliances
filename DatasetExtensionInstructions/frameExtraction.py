import cv2
import numpy as np
import os
import sys

def extractFrames(filename):
    print("Start extract")
    dirName = sys.argv[1].split("/")
    dir = "images_" + dirName[len(dirName) - 1]      # DIR to save IMG
    video = sys.argv[1]+"/"+filename
    print("video: ", video, "  dir: ", dir)

    isExist = os.path.exists(dir)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir)

    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        exit(0)

    #Capture images per 25 frame
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)/fps)
    numberFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #frameFrequency = fps/2.5  # bei ~20 sec duration

    #frameFrequency = 5 # bei ~5 sec duration  => ~ 30 Bilder
    #frameFrequency = 8  # bei ~10 sec duration => ~35 Bilder
    #frameFrequency = 12 # bei ~15 sec duration => ~40 Bilder
    #frameFrequency = 14 # bei ~20 sec duration => ~ 45 Bilder
    #frameFrequency = 15 # bei ~25 sec duration => ~ 50 Bilder
    #frameFrequency = 17 # bei ~30 sec duration => ~ 55 Bilder
    #frameFrequency = 20 # bei ~35 sec duration => ~ 55 Bilder
    #frameFrequency = 40 # bei >40 sec duration
    #frameFrequency = 35 # bei sonstiges
    frameFrequency = 25 # auch bei sonstiges

    ## frameFrequency = fps / (duration * 0,x)
   # frameFrequency = 20
   # if duration <= 20:
   #     frameFrequency = fps/4
   # elif duration <= 30:
   #     frameFrequency = fps/3
   # else:
   #     frameFrequency = fps/2

    print("fps: ", cap.get(cv2.CAP_PROP_FPS))
    print("number of frams: ", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("duration (S): ", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS)))
    print("frame Frequency: ", frameFrequency)
    #frameFrequency=7
    # iterate all frames
    total_frame = 0
    id = 0
    while True:
        ret, frame = cap.read()
        if ret is False:
            break
        total_frame += 1
        if total_frame % frameFrequency == 0:
            id += 1

            image_name = dir + "/" + filename[:-4]+"-"+str(id).zfill(3) + '.jpg'
            cv2.imwrite(image_name, frame)
            print(image_name)

    cap.release()


for filename in os.listdir(sys.argv[1]):
    print("hier: ", filename)
    if filename.endswith(".MOV") or filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".MP4"):
        extractFrames(filename)
        continue
    else:
        continue