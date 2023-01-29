import numpy as np
import cv2
from .plots import Annotator

def constrGlob(im0, line_thickness, names, label, xyxy, seen, glob):

    annotator = Annotator(im0, line_width=line_thickness, example=str(names))
    glob = 'none'                   # if global hint should be visualized: 'cross', 'star', 'flash' or 'none'

    # Value extractions
    p1, p2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
    x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
    y, x = y2 - y1, x2 - x1
    if x > y:
        z = x
    else:
        z = y
    m1, m2 = x1 + int(x/2), y1 + int(y/2)
    e1, e2, e3, e4 = y1-z, x1 - z, x2 + z, y2 + z
    if e1 < 0: e1 = 0
    if e2 < 0: e2 = 0
    if e3 < 0: e3 = 0
    if e4 < 0: e4 = 0
    d1, d2 = int((m1-x1)/3), int((y2-m2)/3)
    if d1 < d2:
        d = d1
    else:
        d = d2
    w = int(d * 2 / 3)
    if w <= 0:
        w = 1

    if glob == 1:                       # gelber Star ohne Füllung, gelbe Umrandung
        # Variables star
        color = (0, 255, 255)           # color of star
        width = w                       # width of the star lines

        # draw
        cv2.line(im0, (m1, y1), (m1, e1), color, width)
        cv2.line(im0, (x2, m2), (e3, m2), color, width)
        cv2.line(im0, (m1, y2), (m1, e4), color, width)
        cv2.line(im0, (x1, m2), (e2, m2), color, width)
        cv2.line(im0, (x2, y1), (e3, e1), color, width)
        cv2.line(im0, (x2, y2), (e3, e4), color, width)
        cv2.line(im0, (x1, y2), (e2, e4), color, width)
        cv2.line(im0, (x1, y1), (e2, e1), color, width)

        annotator.box_label(xyxy, '', color, wVar=width, style='line', gab=0)

    elif glob == 2:                     # roter Kreuz, rote Umrundung, Innen weiß untransparent
        # Variables cross
        color = (0, 0, 255)             # color of cross
        width = w                       # width of the cross lines
        colorFill = (255, 255, 255)     # color of inside

        # draw
        cv2.line(im0, (m1, y1), (m1, e1), color, width)
        cv2.line(im0, (x2, m2), (e3, m2), color, width)
        cv2.line(im0, (m1, y2), (m1, e4), color, width)
        cv2.line(im0, (x1, m2), (e2, m2), color, width)

        cv2.rectangle(im0, p1, p2, colorFill , -1)

        annotator.box_label(xyxy, '', color, wVar=width, style='line', gab=0)

    elif glob == 3:                     # schwarz-weißer Umrandungsflash
        # Variables flash
        color1 = (255, 255, 255)        # color one for the flash
        color2 = (0, 0, 0)              # color two for the flash
        width = w                       # width of the bounding box border

        #draw
        if seen % 2 == 0:               # change every frame
            annotator.box_label(xyxy, '', color1, wVar=width, style='line', gab=0)
        else:
            annotator.box_label(xyxy, '', color2, wVar=width, style='line', gab=0)