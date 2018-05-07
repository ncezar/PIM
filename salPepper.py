import cv2
import numpy as np

#canvas = cv2.imread('lena.jpg',0)





def salPepper(image, pixels):
    #image2= np.zeros((image.shape[0]+2, image.shape[1]+2),np.uint8)

    while(pixels >= 0):
        #print pixels
        x=np.random.randint(0,image.shape[1]-1)
        y=np.random.randint(0,image.shape[0]-1)

        cor=np.random.randint(0, 2)*255

        if image[x][y]!=cor:
            image[x][y]=cor

        pixels-=1


image=cv2.imread ('lena.jpg',0)
#cv2.imshow("Canvas", image)
salPepper(image,100)
cv2.imshow("Canvas", image)
cv2.waitKey(0)
