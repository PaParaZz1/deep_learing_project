# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:26:20 2018

@author: nyz
"""

import json

className={
        3:'car',
        4:'motorbike',
        6:'bus'}
classnum=[3,4,6]

def writeNum(num):
    with open("COCO_train.json","a+") as f:
        f.write(str(num))

inputfile=[]
inner={}

with open("instances_train2014.json","r+") as f:
    allData=json.load(f)
    data=allData["annotations"]
   # print(data[1])
    print("read is ready.")
j=0
for i in data:
    if(i['category_id'] in classnum):
        inner={
            "filename":str(i["image_id"]).zfill(6),
            "name":className[i["category_id"]],
            "bndbox":i["bbox"]
            }
        inputfile.append(inner)
        j+=1
print(j)
inputfile=json.dumps(inputfile)
writeNum(inputfile)