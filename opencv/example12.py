import cv2 as cv
import numpy as np

def template_demo():
    tpl = cv.imread("F:\\pythonwork\\opencv\\1_2.jpg")
    target = cv.imread("F:\\pythonwork\\opencv\\1.jpg")
    cv.imshow("template", tpl)
    cv.imshow("target", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw =tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255,), 2)
        cv.imshow("match-" + np.str(md), target)





print("Hello to Opencv world")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸

t1 = cv.getTickCount()
template_demo()
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(0)

cv.destroyAllWindows()
