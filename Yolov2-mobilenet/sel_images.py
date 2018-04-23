# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:40:12 2018

@author: nyz
"""

import os
import json

nameStr=[]

with open("COCO_train.json","r+") as f:
    data=json.load(f)
    print("read is ready")

for i in data:
    imageName="COCO_train2014_000000"+str(i["filename"])+".jpg"
    nameStr.append(imageName)
    
nameStr=set(nameStr)
#print(nameStr)
print(len(nameStr))

path="D:\\新建文件夹\\train2014\\"
j=0
for file in os.listdir(path):
    if(file not in nameStr):
        os.remove(path+file)
    else:
        j+=1
print(j)