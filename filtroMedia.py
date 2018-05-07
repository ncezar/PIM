import cv2
import numpy as np


def salPepper(image, pixels):
    #image2= np.zeros((image.shape[0]+2, image.shape[1]+2),np.uint8)

    while(pixels >= 0):
        #print pixels
        #print image.shape

        x=np.random.randint(0,image.shape[1]-1)
        y=np.random.randint(0,image.shape[0]-1)

        cor=np.random.randint(0, 2)*255

        if image[x][y]!=cor:
            image[x][y]=cor

        pixels-=1

def media(image, n):
    soma=0
    image2=np.zeros((image.shape[0], image.shape[1]),np.uint8)
    tamanho=n // 2;
    if(n % 2==0): #resto da divisao
        print "Nao rolou!"
    else:#n eh impar
        #image=[]
        #image = image2[1:image2.shape[0]+1, 1:image2.shape[1]+1]
        for y in range(0,image.shape[0]):
            for x in range (0,image.shape[1]):
                #resultado inteiro da divisao
                soma = 0
                for j in range(-tamanho, tamanho):
                    for k in range (-tamanho, tamanho):
                        if y+j >= 0 and y+j < image.shape[0] and x+k >= 0 and x+k < image.shape[1]:
                            soma+=image[y+j][x+k]

                image2[y][x] = soma / (n*n)
    print(tamanho)
    cv2.imshow("Canvas", image2)

    #borda[x][y]= soma





image=cv2.imread('lena.jpg',0)
salPepper(image,2000)

media(image,7)

cv2.waitKey(0)
