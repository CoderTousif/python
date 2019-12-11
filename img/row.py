#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:27:48 2019

@author: sandipan
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import glob
k = 0

new = input("ENTER YOUR INPUT IMAGE DIRECTORY: ")
inpath = os.getcwd() + new
entries = os.listdir(inpath)
for entry in entries:        
#for img in glob('*.png'):
    test_image = cv2.imread(os.path.join(inpath,entry))
    print(entry)

#path='Tp'
#listing=os.listdir(path)
#for file in listing:
#    fname =glob.glob(path+'/'+file+'/*.jpg')
#    print(fname)
#    for fn in fname:
#        test_image=cv2.imread(fn)
#        print(test_image)
    windowsize_r = 5
    windowsize_c = 5
    img = 255 * np.ones((test_image.shape[0],test_image.shape[1],3),np.uint8)
    out_img = 255 * np.ones((test_image.shape[0],test_image.shape[1],3),np.uint8)
    print(img.shape)

    b,g,r = cv2.split(test_image)

#        value=open("value.txt","w")
    for i in range(windowsize_r,test_image.shape[0] - windowsize_r):
        for j in range( windowsize_c,test_image.shape[1] - windowsize_c):
            window_b = b[i-windowsize_r:i+windowsize_r+1,j-windowsize_c:j+windowsize_c+1]
            window_g = g[i-windowsize_r:i+windowsize_r+1,j-windowsize_c:j+windowsize_c+1]
            window_r = r[i-windowsize_r:i+windowsize_r+1,j-windowsize_c:j+windowsize_c+1]
        
        
            mean_b,mean_g,mean_r,_=cv2.mean(test_image[i-windowsize_r:i+windowsize_r+1,j-windowsize_c:j+windowsize_c+1])
            mean_b = np.mean(window_b)
            mean_g = np.mean(window_g)
            mean_r = np.mean(window_r)
        
            if i == 0:
                out_img[i][j] = [int(mean_b),int(mean_g),int(mean_r)]
        
            if i > 0:
                m_b = int(mean_b - out_img[i-1][j][0])
                m_g = int(mean_g - out_img[i-1][j][1])
                m_r = int(mean_r - out_img[i-1][j][2])
            
                if m_b < 0:
                    m_b = (-1) * m_b
            
                if m_g < 0:
                    m_g = (-1) * m_g
            
                if m_r < 0:
                    m_r = (-1) * m_r
                
                out_img[i][j] = [m_b,m_g,m_r]
            
            
            img[i][j] = [int(mean_b),int(mean_g),int(mean_r)]
        #print(int(mean_b),int(mean_g),int(mean_r))
            v = int(mean_b),int(mean_g),int(mean_r)
#            value.write(str(v))
#            value.write("\n")

#    value.close()

#    cv2.imwrite('mean.jpg',img)
#    cv2.imwrite('mean_diff.jpg',out_img)
    out_string = 'a/a/000000'+ str(k)+'.jpg'
    k=k+1
#            cv2.imwrite(os.path.join(outpath,out_arr,out_string),img)
    cv2.imwrite(out_string,out_img)

    