import pyopenpose as op
import argparse
import cv2
import numpy as np
import csv
import pandas as pd
color= (255,0,0)
parser = argparse.ArgumentParser()
args = parser.parse_known_args()
params = dict()
params["model_folder"] = "models/"
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
src = "data/bobo.webm"
cap = cv2.VideoCapture(src)
datum = op.Datum()


   

j=0
with open('outpoints.csv',mode='w') as fin:
    while(True):
        ret, frame = cap.read()  
        dataout = []   
        #bframe= np.zeros(frame.shape, np.uint8)           
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])
        for i in range(25):
            x = int( datum.poseKeypoints[0][i][0] )     
            y = int( datum.poseKeypoints[0][i][1] ) 
            if x == 0 and y == 0 :
                istanza=[j,None,None]
            else :
                istanza = [j,x,y]              
            dataout.append(istanza)                    
        wfin = csv.writer(fin, delimiter=',',quoting=csv.QUOTE_NONE)
        wfin.writerows(dataout)   
        cv2.imshow("prova",datum.cvOutputData)
        k = cv2.waitKey(1)
        j= j+1
        if k==27:
            break;

          



#

#
 
