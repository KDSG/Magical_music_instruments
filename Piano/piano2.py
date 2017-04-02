import cv2
import numpy as np
#from matplotlib  import pyplot as plt
import pygame

pygame.mixer.init()
      
key1,key2,key3,key4,key5,key6,key7,key8=0,0,0,0,0,0,0,0
key9,key10,key11,key12,key13,key14,key15,key16=0,0,0,0,0,0,0,0

pixel1 =0

cap = cv2.VideoCapture(0)


def drawRectangle():
    cv2.rectangle(frame1, (0,220), (30,350), (255,255,255),-1)
    cv2.rectangle(frame1, (40,240), (70,110), (0,0,0),-1)
    cv2.rectangle(frame1, (80,220), (110,350), (255,255,255),-1)
    cv2.rectangle(frame1, (120,240), (150,110), (0,0,0),-1)
    cv2.rectangle(frame1, (160,220), (190,350), (255,255,255),-1)
    cv2.rectangle(frame1, (200,220), (230,350), (255,255,255),-1)
    cv2.rectangle(frame1, (240,240), (270,110), (0,0,0),-1)
    cv2.rectangle(frame1, (280,220), (310,350), (255,255,255),-1)
    cv2.rectangle(frame1, (320,240), (350,110), (0,0,0),-1)
    cv2.rectangle(frame1, (360,220), (390,350), (255,255,255),-1)
    cv2.rectangle(frame1, (400,240), (430,110), (0,0,0),-1)
    cv2.rectangle(frame1, (440,220), (470,350), (255,255,255),-1)
    cv2.rectangle(frame1, (480,220), (510,350), (255,255,255),-1)
    cv2.rectangle(frame1, (520,240), (550,110), (0,0,0),-1)
    cv2.rectangle(frame1, (560,220), (590,350), (255,255,255),-1)
    cv2.rectangle(frame1, (600,240), (630,110), (0,0,0),-1)


while True:
    ret,frame1=cap.read()

    frame = cv2.medianBlur(frame1,5)
    lower=np.array([64,105,40])
    upper=np.array([94,255,250])
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower,upper)
    #res = cv2.bitwise_and(frame,frame, mask = mask)
    roi = mask[330:350,0:30]
    drawRectangle()

##    cv2.imshow('a',frame) 


    fck = cv2.flip(frame1,1)
    cv2.namedWindow("piano", cv2.WINDOW_NORMAL)
    #cv2.setWindowProperty("piano",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_)
    cv2.imshow('piano',fck)
    #nn = cv2.flip(frame1,1)
    #cv2.imshow('c',nn)
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key1 == 0:

        pygame.mixer.music.load("54.wav")
        pygame.mixer.music.play()
        key1 =1
        continue
    if pixel == 0:
        key1 =0
##  Second KEY
    roi = mask[220:240,40:70]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key2 == 0:    
        pygame.mixer.music.load("53.wav")
        pygame.mixer.music.play()
        key2 =1
        continue
    if pixel == 0:
        key2 =0
##  THIRD KEY        
    roi = mask[330:350,80:110]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key3 == 0:
        pygame.mixer.music.load("52.wav")    
        pygame.mixer.music.play()
        key3 =1
        continue
    if pixel == 0:
        key3 =0
        
##  FOURTH KEY
    roi = mask[220:240,120:150]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key4 == 0:    
        pygame.mixer.music.load("51.wav")
        pygame.mixer.music.play()
        key4 =1
        continue
    if pixel == 0:
        key4 =0

    roi = mask[330:350,160:190]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key5 == 0:    
        pygame.mixer.music.load("50.wav")
        pygame.mixer.music.play()
        key5 =1
        continue
    if pixel == 0:
        key5 =0
##  Second KEY
    roi = mask[330:350,200:230]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key6 == 0:    
        pygame.mixer.music.load("49.wav")
        pygame.mixer.music.play()
        key6 =1
        continue
    if pixel == 0:
        key6 =0
##  THIRD KEY        
    roi = mask[220:240,240:270]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key7 == 0:
        pygame.mixer.music.load("48.wav")    
        pygame.mixer.music.play()
        key7 =1
        continue
    if pixel == 0:
        key7 =0
        
##  FOURTH KEY
    roi = mask[330:350,280:310]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key8 == 0:    
        pygame.mixer.music.load("47.wav")
        pygame.mixer.music.play()
        key8 =1
        continue
    if pixel == 0:
        key8 =0

    roi = mask[220:240,320:350]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key9 == 0:    
        pygame.mixer.music.load("46.wav")
        pygame.mixer.music.play()
        key9 =1
        continue
    if pixel == 0:
        key9 =0
##  Second KEY
    roi = mask[330:350,360:390]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key10 == 0:    
        pygame.mixer.music.load("45.wav")
        pygame.mixer.music.play()
        key10 =1
        continue
    if pixel == 0:
        key10 =0
##  THIRD KEY        
    roi = mask[220:240,400:430]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key11 == 0:
        pygame.mixer.music.load("44.wav")    
        pygame.mixer.music.play()
        key11 =1
        continue
    if pixel == 0:
        key11 =0
        
##  FOURTH KEY
    roi = mask[330:350,440:470]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key12 == 0:    
        pygame.mixer.music.load("43.wav")
        pygame.mixer.music.play()
        key12 =1
        continue
    if pixel == 0:
        key12 =0

    roi = mask[330:350,480:510]    
    for frame in roi:
        for pixel in frame:
            if pixel == 255: 
                break            
    if pixel ==255 and key13 == 0:    
        pygame.mixer.music.load("42.wav")
        pygame.mixer.music.play()
        key13 =1
        continue
    if pixel == 0:
        key13 =0
##  Second KEY
    roi = mask[220:240,520:550]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key14 == 0:    
        pygame.mixer.music.load("41.wav")
        pygame.mixer.music.play()
        key14 =1
        continue
    if pixel == 0:
        key14 =0
##  THIRD KEY        
    roi = mask[330:350,560:590]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key15 == 0:
        pygame.mixer.music.load("40.wav")    
        pygame.mixer.music.play()
        key15 =1
        continue
    if pixel == 0:
        key15 =0
        
##  FOURTH KEY
    roi = mask[220:240,600:630]
    for frame in roi:
        for pixel in frame:
            if pixel == 255:
                break            
    if pixel ==255 and key16 == 0:    
        pygame.mixer.music.load("39.wav")
        pygame.mixer.music.play()
        key16 =1
        continue
    if pixel == 0:
        key16 =0
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    