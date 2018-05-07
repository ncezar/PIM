import cv2
import numpy as np




def mediana(img):
    #median=np.zeros((img.shape[0], img.shape[1]),np.uint8)
    final = cv2.medianBlur(img, 3)
    cv2.imshow('Median Blur',final)





img = cv2.imread('SalPepper.png',0)
mediana(img)


cv2.waitKey(0)
