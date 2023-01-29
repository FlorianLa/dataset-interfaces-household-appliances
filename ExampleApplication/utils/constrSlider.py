import numpy as np
import cv2
from .plots import Annotator

def constrSlider(im0, line_thickness, names, label, xyxy, seen, slider):

    annotator = Annotator(im0, line_width=line_thickness, example=str(names))
    glob = 'none'                   # if global hint should be visualized: 'cross', 'star', 'flash' or 'none'
    # Value extractions
    p1, p2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
    x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
    y, x = y2 - y1, x2 - x1
    if x > y:
        z = x
        side = ['above', 'under']               # right or above
    else:
        z = y
        side = ['right', 'left']                # left or under
    m1, m2 = x1 + int(x/2), y1 + int(y/2)
    e1, e2, e3, e4 = y1-z, x1 - z, x2 + z, y2 + z
    if e1 < 0: e1 = 0
    if e2 < 0: e2 = 0
    if e3 < 0: e3 = 0
    if e4 < 0: e4 = 0
    d1, d2 = int((m1-x1)/3), int((y2-m2)/3)
    if d1 < d2:
        d = d1
        nd = d2
    else:
        d = d2
        nd = d1
    w = int(d * 2 / 3)
    if w <= 0:
        w = 1

    if slider == 1:                 # pink gepunktete Umrandung, gelber Pfeil mit Dreieckspitzen unten
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'dotted'        # dotted or dashed
        gab = 100                   # gab for dotted / dashed
        colorBorder = (255, 0, 255) # color of the border BGR
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

        # arrow
        position = 0                # where the arrow is positioned: 'right', 'left', 'above', 'under'
        dis = 0                     # Distance of arrow to border (recommended: 0, d1 if 'left' or 'right', d2 if 'above' or 'under')
        color = (0, 255, 255)       # color of arrow
        aboveright = 'triangle'     # right or upper arrowhead ('line', 'triangle', 'none')
        underleft = 'triangle'      # under or left arrowhead ('line', 'triangle', 'none')
        colorAboveR = (0, 255, 255) # color of right or upper arrowhead
        colorUnderL = (0, 255, 255) # color arrowhead under left
        width = w                   # width in pxl of arrow
        aboveRWidth = w             # width in pxl of upper or right arrowhead (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of under or left arrowhead (only if arrowhead == 'line')

    elif slider == 2:               # rote gestrichelte Umrandung, weißer Pfeil mit dünnen Pfeilspitzen unten
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'dashed'        # dotted or dashed
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

        # arrow
        position = 1                # where the arrow is positioned: 'right', 'left', 'above', 'under'
        dis = 0                     # Distance of arrow to border (recommended: 0, d1 if 'left' or 'right', d2 if 'above' or 'under')
        color = (255, 255, 255)     # color of arrow
        aboveright = 'line'         # right or upper arrowhead ('line', 'triangle', 'none')
        underleft = 'line'          # under or left arrowhead ('line', 'triangle', 'none')
        colorAboveR = (255, 255, 255)# color of right or upper arrowhead
        colorUnderL = (255, 255, 255)# color arrowhead under left
        width = w                   # width in pxl of arrow
        aboveRWidth = w             # width in pxl of upper or right arrowhead (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of under or left arrowhead (only if arrowhead == 'line')

    # draw
    if border == "full":
        annotator.box_label(xyxy, labelVal, colorBorder, wVar=borderWidth, style=styleLine, gab=gab)  # AUSPROBIEREN DAS NACH UNTEN MIT FÜLLUNG

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
        cop1 = im0.copy()  # AUSPROBIEREN OB HIER AUCH OHNE COP GEHT!!!
        cv2.rectangle(cop1, p1, p2, colorFill1, -1)
        cv2.addWeighted(cop1, a1, im0, b1, 0, im0)

    if numbFill2:
        cop2 = im0.copy()
        cv2.rectangle(cop2, (d1 + x1, y1 + d2), (x2 - d1, y2 - d2), colorFill2, -1)
        cv2.addWeighted(cop2, a2, im0, b2, 0, im0)

    if numbFill3:
        cop3 = im0.copy()
        cv2.rectangle(cop3, (m1 - d1, m2 - d2), (m1 + d1, m2 + d2), colorFill3, -1)
        cv2.addWeighted(cop3, a3, im0, b3, 0, im0)

    add1 = abs(nd - d) * 2
    addO = int(nd / 3)
    addU = int(nd / 3)
    ndU = nd
    ndO = nd
    addL = 0
    #nd = int(nd/2)

    if side[position] == 'left':
        cv2.line(im0, (x1 - dis, y1), (x1 - dis, y2), color, width)
        if aboveright == 'line':
            cv2.line(im0, (x1 - dis, y1), (x1 - d1 - dis, y1 + d2 - addO), colorAboveR, aboveRWidth)
            cv2.line(im0, (x1 - dis, y1), (x1 + d1 - dis, y1 + d2 - addO), colorAboveR, aboveRWidth)

        elif aboveright == 'triangle':
            triangle = np.array([(x1 - dis, y1 - nd), (x1 - d1 - dis, y1 + d2 - addO), (x1 + d1 - dis, y1 + d2 - addO)])
            cv2.drawContours(im0, [triangle], 0, colorAboveR, -1)

        if underleft == 'line':
            cv2.line(im0, (x1 - dis, y2), (x1 - d1 - dis, y2 - d2 + addU), colorUnderL, underLWidth)
            cv2.line(im0, (x1 - dis, y2), (x1 + d1 - dis, y2 - d2 + addU), colorUnderL, underLWidth)

        elif underleft == 'triangle':
            tria = np.array([(x1 - dis, y2 + nd), (x1 - d1 - dis, y2 - d2 + addU), (x1 + d1 - dis, y2 - d2 + addU)])
            cv2.drawContours(im0, [tria], 0, colorUnderL, -1)

    elif side[position] == 'right':
        cv2.line(im0, (x2 + dis, y1), (x2 + dis, y2), color, width)
        if aboveright == 'line':
            cv2.line(im0, (x2 + dis, y1), (x2 - d1 + dis, y1 + d2 - addO), colorAboveR, aboveRWidth)
            cv2.line(im0, (x2 + dis, y1), (x2 + d1 + dis, y1 + d2 - addO), colorAboveR, aboveRWidth)

        elif aboveright == 'triangle':
            triangle = np.array([(x2 + dis, y1 - nd), (x2 - d1 + dis, y1 + d2 - addO), (x2 + d1 + dis, y1 + d2 - addO)])
            cv2.drawContours(im0, [triangle], 0, colorAboveR, -1)

        if underleft == 'line':
            cv2.line(im0, (x2 + dis, y2), (x2 - d1 + dis, y2 - d2 + addU), colorUnderL, underLWidth)
            cv2.line(im0, (x2 + dis, y2), (x2 + d1 + dis, y2 - d2 + addU), colorUnderL, underLWidth)

        elif underleft == 'triangle':
            tria = np.array([(x2 + dis, y2 + nd), (x2 - d1 + dis, y2 - d2 + addU), (x2 + d1 + dis, y2 - d2 + addU)])
            cv2.drawContours(im0, [tria], 0, colorUnderL, -1)

    elif side[position] == 'above':
        cv2.line(im0, (x1, y1 - dis), (x2, y1 - dis), color, width)
        if aboveright == 'line':  # TESTEN
            cv2.line(im0, (x2, y1 - dis), (x2 - d1, y1 - d2 - dis - addO), colorAboveR, aboveRWidth)
            cv2.line(im0, (x2, y1 - dis), (x2 - d1, y1 + d2 - dis + addO), colorAboveR, aboveRWidth)

        elif aboveright == 'triangle':
            triangle = np.array([(x2 + nd, y1 - dis), (x2 - d1, y1 - d2 - dis - addO), (x2 - d1, y1 + d2 - dis + addO)])
            cv2.drawContours(im0, [triangle], 0, colorAboveR, -1)

        if underleft == 'line':
            cv2.line(im0, (x1, y1 - dis), (x1 + d1, y1 - d2 - dis - addU), colorUnderL, underLWidth)
            cv2.line(im0, (x1, y1 - dis), (x1 + d1, y1 + d2 - dis + addU), colorUnderL, underLWidth)

        elif underleft == 'triangle':
            tria = np.array([(x1 - nd, y1 - dis), (x1 + d1, y1 - d2 - dis - addU), (x1 + d1, y1 + d2 - dis + addU)])
            cv2.drawContours(im0, [tria], 0, colorUnderL, -1)

    elif side[position] == 'under':
        cv2.line(im0, (x1, y2 + dis), (x2, y2 + dis), color, width)
        if aboveright == 'line':
            cv2.line(im0, (x2, y2 + dis), (x2 - d1, y2 - d2 + dis - addO), colorAboveR, aboveRWidth)
            cv2.line(im0, (x2, y2 + dis), (x2 - d1, y2 + d2 + dis + addO), colorAboveR, aboveRWidth)

        elif aboveright == 'triangle':
            triangle = np.array([(x2 + nd, y2 + dis), (x2 - d1, y2 - d2 + dis - addO), (x2 - d1, y2 + d2 + dis + addO)])
            cv2.drawContours(im0, [triangle], 0, colorAboveR, -1)

        if underleft == 'line':
            cv2.line(im0, (x1, y2 + dis), (x1 + d1, y2 - d2 + dis - addU), colorUnderL, underLWidth)
            cv2.line(im0, (x1, y2 + dis), (x1 + d1, y2 + d2 + dis + addU), colorUnderL, underLWidth)

        elif underleft == 'triangle':
            tria = np.array([(x1 - nd, y2 + dis), (x1 + d1, y2 - d2 + dis - addU), (x1 + d1, y2 + d2 + dis + addU)])
            cv2.drawContours(im0, [tria], 0, colorUnderL, -1)

