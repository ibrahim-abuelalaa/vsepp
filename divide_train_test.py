# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:06:56 2018

@author: ibrahim
"""

from sklearn.cross_validation import train_test_split
import glob
import csv

imgs = glob.glob('/home/ibrahim/vsepp/cub/images/*.jpg')

train, test = train_test_split(imgs)

train, val = train_test_split(train)


#
#
#with open('train.csv', 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(train)
#    
#with open('test.csv', 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(test)
#
#with open('test.csv', 'rb') as f:
#    reader = csv.reader(f)
#    train = list(reader)[0]

#with open('test.csv', 'rb') as f:
#    reader = csv.reader(f)
#    test = list(reader)[0]


    
json_dict= {'images':[]}
i=0

#print test[0]
for img in test:
    json_dict['images'].append({'filename':img.split('/home/ibrahim/vsepp/cub/images/')[1],'sentences':[],'split':'test' })
    with open('/home/ibrahim/Downloads/cvpr2016_cub/text_c10/text/'+img.split('/home/ibrahim/vsepp/cub/images/')[1].split('.jpg')[0]+'.txt', 'rb') as f:
        content = f.readlines()
    
    for cap in content:
        json_dict['images'][i]['sentences'].append({'raw':cap})
    i = i+ 1
    
for img in train:
    json_dict['images'].append({'filename':img.split('/home/ibrahim/vsepp/cub/images/')[1],'sentences':[],'split':'train' })
    with open('/home/ibrahim/Downloads/cvpr2016_cub/text_c10/text/'+img.split('/home/ibrahim/vsepp/cub/images/')[1].split('.jpg')[0]+'.txt', 'rb') as f:
        content = f.readlines()
    
    for cap in content:
        json_dict['images'][i]['sentences'].append({'raw':cap})
    i = i+ 1

for img in val:
    json_dict['images'].append({'filename':img.split('/home/ibrahim/vsepp/cub/images/')[1],'sentences':[],'split':'val' })
    with open('/home/ibrahim/Downloads/cvpr2016_cub/text_c10/text/'+img.split('/home/ibrahim/vsepp/cub/images/')[1].split('.jpg')[0]+'.txt', 'rb') as f:
        content = f.readlines()
    
    for cap in content:
        json_dict['images'][i]['sentences'].append({'raw':cap})
    i = i+ 1
    
import json
with open('CUB.json', 'w') as fp:
    json.dump(json_dict, fp)
