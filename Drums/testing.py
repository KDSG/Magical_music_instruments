import cv2
import numpy as np
from matplotlib  import pyplot as plt
import pygame
pygame.mixer.init()

img1 = cv2.imread("d2.png")
img2 = cv2.imread("d3.png")
img3 = cv2.imread("d4.png")
imm = cv2.imread("cool.png")
key1 =0
ke=0
key2 = 0
key3 =0
key4=0
pixel1 =0
#cv2.namedWindow('a',cv2.WINDOW_NORMAL)
cv2.imshow('a',imm)
cv2.waitKey(0)
cv2.destroyAllWindows()
while True:
    #cv2.namedWindow('a',cv2.WINDOW_NORMAL)
    cv2.imshow('a',img1)
    pygame.mixer.music.load("desi(2).wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() :
        if cv2.waitKey(1) & 0xFF == ord('g'):
            ke = 1
            pygame.mixer.quit()
            break
        else:
            continue    
    
    if ke == 1:
        break
    
    cv2.imshow('a',img2)
    pygame.mixer.music.load("desi(3).wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() :
        if cv2.waitKey(1) & 0xFF == ord('g'):
            ke = 1
            pygame.mixer.quit()
            break
        else:
            continue    
    
    if ke == 1:
        break

    cv2.imshow('a',img3)
    pygame.mixer.music.load("desi(4).wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() :
        if cv2.waitKey(1) & 0xFF == ord('g'):
            ke = 1
            pygame.mixer.quit()
            break
        else:
            continue    
    
    if ke == 1:
        break
pygame.mixer.init()
cap = cv2.VideoCapture(0)
cv2.namedWindow('a',cv2.WINDOW_NORMAL)
while True:
    
    ret,frame=cap.read()
    cv2.rectangle(frame,(67,37),(170,38),(0,0,255),0)
    cv2.rectangle(frame,(57,327),(154,328),(0,0,255),0)
    cv2.rectangle(frame,(487,327),(584,328),(0,0,255),0)
    cv2.rectangle(frame,(257,307),(404,308),(0,0,255),0)    

 #   frame = cv2.medianBlur(frame,3)
    
    lower=np.array([64,105,40])
    upper=np.array([94,255,255])
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(hsv,lower,upper)
    res = cv2.bitwise_and(frame,frame,mask = mask)
#    frame = cv2.medianBlur(res,3)

    img2=cv2.imread('crash.jpg')
    rows,cols,channels = img2.shape

    rof=frame[0:rows,60:cols+60]
    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask1=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask1)
    img1_bg=cv2.bitwise_and(rof,rof,mask=mask_inv)
    img2_fg=cv2.bitwise_and(img2,img2,mask=mask1)
    dst=cv2.add(img1_bg,img2_fg)
    frame[0:rows,60:cols+60]=dst

    img2=cv2.imread('floortom.jpg')
    rows,cols,channels = img2.shape

    rof=frame[295:rows+295,250:cols+250]
    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask1=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask1)
    img1_bg=cv2.bitwise_and(rof,rof,mask=mask_inv)
    img2_fg=cv2.bitwise_and(img2,img2,mask=mask1)
    dst=cv2.add(img1_bg,img2_fg)
    frame[295:rows+295,250:cols+250]=dst
    rows,cols,channels = img2.shape


    img2=cv2.imread('snare.jpg')
    rows,cols,channels = img2.shape

    rof=frame[314:rows+314,480:cols+480]
    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask1=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask1)
    img1_bg=cv2.bitwise_and(rof,rof,mask=mask_inv)
    img2_fg=cv2.bitwise_and(img2,img2,mask=mask1)
    dst=cv2.add(img1_bg,img2_fg)
    frame[314:rows+314,480:cols+480]=dst

    img2=cv2.imread('tom.jpg')
    rows,cols,channels = img2.shape

    rof=frame[320:rows+320,50:cols+50]
    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask1=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask1)
    img1_bg=cv2.bitwise_and(rof,rof,mask=mask_inv)
    img2_fg=cv2.bitwise_and(img2,img2,mask=mask1)
    dst=cv2.add(img1_bg,img2_fg)
    frame[320:rows+320,50:cols+50]=dst
    

#    mask=cv2.inRange(med,lower,upper)
    
    roi = mask[27:32,67:170]
    frame = cv2.flip(frame,1)
    cv2.imshow('a',frame)
#    cv2.imshow('b',mask)
  #  cv2.imshow('c',med)
    for frame in roi:
        for pixel in frame:
            if pixel == 255:    
                break
            
    if pixel ==255 and key1 == 0:    
        pygame.mixer.music.load("a1.wav")
        pygame.mixer.music.play()
        key1 =1
        continue
    if pixel == 0:
        key1 = 0
##  Second KEY
    roi = mask[327:332,57:154]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key2 == 0:    
        pygame.mixer.music.load("a2.wav")
        pygame.mixer.music.play()
        key2 =1
        continue
    if pixel == 0:
        key2 =0
##  THIRD KEY        
    roi = mask[327:332,487:584]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key3 == 0:    
        pygame.mixer.music.load("a3.wav")
        pygame.mixer.music.play()

        key3 =1
        continue
    if pixel == 0:
        key3 =0
        
##  FOURTH KEY
    roi = mask[307:312,257:404]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key4 == 0:    
        pygame.mixer.music.load("a4.wav")
        pygame.mixer.music.play()
        key4 =1
        continue
    if pixel == 0:
        key4 =0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
