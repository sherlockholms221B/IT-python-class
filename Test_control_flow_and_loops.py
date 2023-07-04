# for loops


import os 
import time, cv2 as cv
import sys


labels = ['thumbsup','thanks','welcome','home']
ImagePath = os.path.join('frontend','builds')
how_many_time=4

#create base dir
if not os.path.exists(ImagePath):
    if os.name == 'nt':
        os.makedirs(ImagePath)
        
#create sub dir
for label in labels:
    print(label)
    img_dir = os.path.join(ImagePath,label)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
        
for label in labels:
    print('opening cv2 for {}'.format(label))
    cap = cv.VideoCapture(0)
    time.sleep(5)
    for img_num in range(how_many_time):
        ret ,frame = cap.read()
        cv.imshow('picture',frame)
        cv.imwrite(os.path.join(ImagePath,label,label+str(img_num)+'.jpg'),frame)
        print(frame)
cv.waitKey(0)
cv.destroyAllWindows()

