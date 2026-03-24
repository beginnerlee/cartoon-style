import cv2 as cv
import numpy as np

img = cv.imread('dolphin.PNG')
imgthresholdtype=cv.THRESH_BINARY

#Bilateral Filter 변수
kernelsize=9
sigmacolor=250
sigmaspace=250


#Thresholding 변수
adaptivetype=cv.ADAPTIVE_THRESH_MEAN_C
adaptiveblocksize=9
adaptivec=9


while True:
    #median blur 및 thresholding 수행
    bw=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    bwblur=cv.medianBlur(bw, 3)
    edge=cv.adaptiveThreshold(bwblur,255,adaptivetype,imgthresholdtype,adaptiveblocksize,adaptivec)

    # Bilateral Filter 적용
    for i in range(15):
        color_simple = cv.bilateralFilter(img,kernelsize,sigmacolor,sigmaspace)

    #선을 더 굵게 만들기 위해 침식 연산 수행
    kernel = np.ones((2, 2), np.uint8)
    edge_sharp = cv.erode(edge, kernel, iterations=1)
    cartoon=cv.bitwise_and(color_simple,color_simple, mask=edge_sharp)

    #원본 이미지와 cartoon style로 변형한 이미지를 출력하여 비교
    cv.imshow('original', img)
    cv.imshow('Cartoon Style', cartoon)

    #esc를 누르면 종료 후 이미지 저장
    key=cv.waitKey(0)
    if key==27:
        cv.imwrite('cartoonstyle.png', cartoon)
        break

cv.destroyAllWindows()

