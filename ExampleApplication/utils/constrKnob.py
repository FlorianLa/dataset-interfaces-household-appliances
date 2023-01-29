import numpy as np
import cv2
from .plots import Annotator

def constrKnob(im0, line_thickness, names, label, xyxy, seen, knob):

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
        nd = d2
    else:
        d = d2
        nd = d1
    w = int(d * 2 / 3)
    if w <= 0:
        w = 1



    if knob == 1:                   # weiß transparent, roter Pfeil, doppel Dreieck-Spitze, oben, entfernt
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'none'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "none"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = True            # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

        # arrow
        above = True                # if an arrow above is drawn
        under = False               # if an arrow under is drawn
        aboveDis = d2               # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'triangle'      # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'none'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (0, 0, 255)    # color arrow above
        colorAboveR = (0, 0, 255)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 0, 255)    # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255)   # color arrowhead under left
        aboveWidth = w               # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w               # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 2:                 # roter Pfeil, unten, nach rechts, dünne Spitze
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'none'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "none"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
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
        above = False               # if an arrow above is drawn
        under = True                # if an arrow under is drawn
        aboveDis = d2               # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'triangle'      # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'line'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'none'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (0, 0, 255)    # color arrow above
        colorAboveR = (0, 0, 255)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 0, 255)    # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255)   # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 3:                 # blauer Pfeil, oben, ohne Abstand, rechts Dreieckspitze
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'none'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "none"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
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
        above = True                # if an arrow above is drawn
        under = False               # if an arrow under is drawn
        aboveDis = 0                # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'none'          # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'none'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (255, 0, 0)    # color arrow above
        colorAboveR = (255, 0, 0)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 0, 255)    # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255)   # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 4:                 # oranger    Pfeilkreis, Dreieckspitzen im Uhrzeigersinn
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'none'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "none"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
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
        above = True                # if an arrow above is drawn
        under = True                # if an arrow under is drawn
        aboveDis = 0                # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'line'         # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'none'          # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'line'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (0, 0, 255)  # color arrow above
        colorAboveR = (0, 0, 255) # color arrowhead above right
        colorAboveL = (0, 100, 2)   # color arrowhead above left
        colorUnder = (0, 0, 255)  # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255) # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 5:                 # dunkel transparent, gelber Pfeil unten ohne Abstand mit dünner Pfeilspitze links
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'none'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 255)   # color of the border BGR
        border = "none"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = True            # if inside complete should be filled
        colorFill1 = (0, 0, 0)      # color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

        # arrow
        above = False               # if an arrow above is drawn
        under = True                # if an arrow under is drawn
        aboveDis = d2               # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'triangle'      # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'line'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (0, 0, 255)    # color arrow above
        colorAboveR = (0, 0, 255)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 255, 255)  # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 255, 255) # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 6:                 # gelbe Umrandung, blauer Pfeil oben, ohne Abstand, rechts Dreieckspitze
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 255, 255) # color of the border BGR
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
        above = True                # if an arrow above is drawn
        under = False               # if an arrow under is drawn
        aboveDis = 0                # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'none'          # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'none'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (255, 0, 0)    # color arrow above
        colorAboveR = (255, 0, 0)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 0, 255)    # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255)   # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

    elif knob == 7:                 # weiß transparent, schwarte Umrandung, roter Pfeil oben ohne Abstand, doppel Dreieckspitze
        # border
        labelVal = ''               # label[:-5] or label
        styleLine = 'line'          # 'dotted', 'dashed' or 'line'
        gab = 100                   # gab for dotted / dashed
        colorBorder = (0, 0, 0)     # color of the border BGR
        border = "full"             # border typ: full -> full around, corner -> only in all 4 corners, none -> no border
        borderWidth = w             # width in pxl of border (if box filled, half of border is inside)

        # inside
        numbFill1 = True            # if inside complete should be filled
        colorFill1 = (255, 255, 255)# color of the inside complete
        a1, b1 = 0.5, 0.5           # ratio alpha of inside (a1), alpha of background (b1) -> degree of transparency
        numbFill2 = False           # if inside middle should be filled
        colorFill2 = (122, 25, 25)  # color of inside middle
        a2, b2 = 0.8, 0.2           # ratio transparency of inside middle
        numbFill3 = False           # if inside little should be filles
        colorFill3 = (255, 0, 255)  # color of inside little
        a3, b3 = 0.4, 0.6           # ratio transparency of inside little

        # arrow
        above = True                # if an arrow above is drawn
        under = False               # if an arrow under is drawn
        aboveDis = 0                # Distance of arrow above to border (recommended: 0 or d2)
        underDis = 0                # Distance of arrow under to border (recommended 0 or d2)
        aboveright = 'triangle'     # Arrowhead above right to border ('line', 'triangle', 'none')
        aboveleft = 'triangle'      # Arrowhead above left to border ('line', 'triangle', 'none')
        underright = 'none'         # Arrowhead under right to border ('line', 'triangle', 'none')
        underleft = 'none'          # Arrowhead under left to border ('line', 'triangle', 'none')
        colorAbove = (0, 0, 255)    # color arrow above
        colorAboveR = (0, 0, 255)   # color arrowhead above right
        colorAboveL = (0, 0, 255)   # color arrowhead above left
        colorUnder = (0, 0, 255)    # color arrow under
        colorUnderR = (0, 0, 255)   # color arrowhead under right
        colorUnderL = (0, 0, 255)   # color arrowhead under left
        aboveWidth = w              # width in pxl of arrow above
        aboveRWidth = w             # width in pxl of arrowhead above right (only if arrowhead == 'line')
        aboveLWidth = w             # width in pxl of arrowhead above left (only if arrowhead == 'line')
        underWidth = w              # width in pxl of arrow under
        underRWidth = w             # width in pxl of arrowhead under right (only if arrowhead == 'line')
        underLWidth = w             # width in pxl of arrowhead under left (only if arrowhead == 'line')

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

    add1 = abs(nd-d)*2
    addO = int(nd/2)
    addU = int(nd/2)
    ndU = nd
    ndO = nd
    addL = 0

    if above:
        cv2.ellipse(im0, (m1, m2 - aboveDis), (int(z / 2), int(z / 2)), 0, 0, -180, colorAbove, aboveWidth)
        if aboveright == 'line':
            cv2.line(im0, (x2+add1, m2 - aboveDis), (x2 +add1+ d1, m2 +addL- d2 - aboveDis), colorAboveR, aboveRWidth)
            cv2.line(im0, (x2+add1, m2 - aboveDis), (x2 +add1- d1, m2+addL - d2 - aboveDis), colorAboveR, aboveRWidth)

        elif aboveright == 'triangle':
            triangle = np.array([(x2+add1, m2+ndO - aboveDis), (x2+ add1+d1, m2+addO - d2 - aboveDis),
                                 (x2 +add1- d1, m2+addO - d2 - aboveDis)])  # VERHÄLTNISMÄSSIG BEI ERSTEN Y_WERT HINZUFÜGEN
            cv2.drawContours(im0, [triangle], 0, colorAboveR, -1)

        if aboveleft == 'line':
            cv2.line(im0, (x1-add1, m2 - aboveDis), (x1 -add1- d1, m2 +addL- d2 - aboveDis), colorAboveL, aboveLWidth)
            cv2.line(im0, (x1-add1, m2 - aboveDis), (x1 -add1+ d1, m2 +addL- d2 - aboveDis), colorAboveL, aboveLWidth)

        elif aboveleft == 'triangle':
            tria = np.array([(x1-add1, m2+ndO - aboveDis), (x1-add1+ d1, m2 + addO - d2 - aboveDis),
                             (x1-add1 - d1, m2 + addO - d2 - aboveDis)])
            cv2.drawContours(im0, [tria], 0, colorAboveL, -1)

    if under:
        cv2.ellipse(im0, (m1, m2 + underDis), (int(z / 2), int(z / 2)), 0, 0, 180, colorUnder, underWidth)
        if underright == 'line':
            cv2.line(im0, (x2+add1, m2 + underDis), (x2 +add1+ d1, m2 -addL + d2 + underDis), colorUnderR, underRWidth)
            cv2.line(im0, (x2+add1, m2 + underDis), (x2+add1 - d1, m2 -addL + d2 + underDis), colorUnderR, underRWidth)

        elif underright == 'triangle':
            triangle = np.array(
                [(x2+add1, m2-ndU + underDis), (x2 +add1+ d1, m2-addU + d2 + underDis), (x2 +add1- d1, m2-addU + d2 + underDis)])
            cv2.drawContours(im0, [triangle], 0, colorUnderR, -1)

        if underleft == 'line':
            cv2.line(im0, (x1-add1, m2 + underDis), (x1-add1 - d1, m2 -addL + d2 + underDis), colorUnderL, underLWidth)
            cv2.line(im0, (x1-add1, m2 + underDis), (x1-add1 + d1, m2 -addL + d2 + underDis), colorUnderL, underLWidth)

        elif underleft == 'triangle':
            tri = np.array([(x1-add1, m2 -ndU + underDis), (x1 -add1 + d1, m2 -addU+ d2 + underDis),
                            (x1 -add1 - d1, m2 -addU + d2 + underDis)])
            cv2.drawContours(im0, [tri], 0, colorUnderL, -1)
