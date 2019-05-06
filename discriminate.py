from builtins import range

import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import Counter

def inform_state(image):
    img_scr = cv2.imread(image)
    img_hsv = cv2.cvtColor(img_scr, cv2.COLOR_BGR2HSV)

    height = img_hsv.shape[0]
    width = img_hsv.shape[1]
    pixels = []
    sick_parameter = 0


    for y in range(0, height, 10):
        for x in range(0, width, 10):
            if (img_hsv[y, x, 1] > 45 and 32 < img_hsv[y, x, 2]):
                pixels.append(img_hsv[y, x, 0])
            else:
                sick_parameter += 1

    plt.xlim(0, 180)
    plt.xticks([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])
    plt.hist(pixels, bins=12, range=(0, 180))

    bins = np.linspace(0, 180, 13)

    index = np.digitize(pixels, bins)
    c = Counter(index)
    print(c)
    mode = c.most_common(1)
    print(sick_parameter)

    if not mode:  # modeの配列に値が入ってない場合（画像が真っ白とかの場合）
         print("発芽していません") # False

    else:
        if 3 in c.keys():  # modeの中身が入っていて緑の要素が含まれていない場合を考慮する。
            if c[3] > 100:  # 緑の要素の値が100以上含まれていた場合
                if sick_parameter > 10000:
                    print("病気の恐れがあります") #発芽してるけど病気
                else:
                    print("発芽しています")  # True
            else:
                print("発芽していません")  # False
        else:
            print("発芽していません")  # False
