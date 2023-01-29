import numpy as np
import cv2
from .plots import Annotator

def constrPush(im0, line_thickness, names, label, xyxy, seen, push):

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
    w = int(d*2/3)
    if w <= 0:
        w = 1



    if push == 1:                   # rote Umrandung, label Push

        # border
        labelVal = 'Push'           # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = int(d*100)            # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = False           # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 2:                 # rote Umrandung

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = False           # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 3:                 # Ecken Umrandung, gelb

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 255, 255) # color of the border BGR
        border = 'corner'           # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = False           # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 4:                 # blauer Rand, mittel groß Transparent gelb

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (255, 0, 0)   # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = False           # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = True            # if inside middle should be filled
        colorFill2 = (0, 255, 255)  # color of inside middle
        a2, b2 = 0.6, 0.4           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 5:                 # weißer Rand, dunkle Füllung transparent

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (255, 255, 255)# color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = True            # if inside complete should be filled
        colorFill1 = (112, 25, 25)  # color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 6:                 # pinker Rand, dunkel transparent mitte, heller transparent innen

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (255, 0, 255) # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = False           # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = True            # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = True            # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    elif push == 7:                 # orange ausgefüllt, dunkel orangener Rand

        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 100, 200) # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = True            # if inside complete should be filled
        colorFill1 = (0, 165, 255)  # color of the inside complete
        a1, b1 = 1., 0.0            # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

    # draw
    if border == "full":
        annotator.box_label(xyxy, labelVal, colorBorder, wVar=borderWidth, style=styleLine, gab=gab)       # AUSPROBIEREN DAS NACH UNTEN MIT FÜLLUNG

    elif border == "corner":  # EVENTUELL EINZELN FÄRBEN ODER GLEICHZEITIG MIT BORDER MÖGLICH MACHEN
        cv2.line(im0, (x1, y1), (m1 - d1, y1), colorBorder, borderWidth)
        cv2.line(im0, (x1, y1), (x1, m2 - d2), colorBorder, borderWidth)
        cv2.line(im0, (x2, y1), (m1 + d1, y1), colorBorder, borderWidth)
        cv2.line(im0, (x2, y1), (x2, m2 - d2), colorBorder, borderWidth)
        cv2.line(im0, (x1, y2), (x1, m2 + d2), colorBorder, borderWidth)
        cv2.line(im0, (x1, y2), (m1 - d1, y2), colorBorder, borderWidth)
        cv2.line(im0, (x2, y2), (m1 + d1, y2), colorBorder, borderWidth)
        cv2.line(im0, (x2, y2), (x2, m2 + d2), colorBorder, borderWidth)

    if numbFill1:
        cop1 = im0.copy()                                       # AUSPROBIEREN OB HIER AUCH OHNE COP GEHT!!!
        cv2.rectangle(cop1, p1, p2, colorFill1, -1)
        cv2.addWeighted(cop1, a1, im0, b1, 0, im0)

    if numbFill2:
        cop2 = im0.copy()
        cv2.rectangle(cop2, (d1+x1, y1+d2), (x2-d1, y2-d2), colorFill2, -1)
        cv2.addWeighted(cop2, a2, im0, b2, 0, im0)

    if numbFill3:
        cop3 = im0.copy()
        cv2.rectangle(cop3, (m1-d1, m2-d2), (m1+d1, m2+d2), colorFill3, -1)
        cv2.addWeighted(cop3, a3, im0, b3, 0, im0)
