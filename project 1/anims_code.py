"""
Created on Mon Aug 24 19:49:19 2020

@author: Sivaraman Sivaraj
"""

import numpy as np, os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

name = input("Enter the being which you like the most animal/bird/reptile ? \n\n" )

name = name.lower()
###################################################
###################################################
being_list = ['elephant', 'lion', 'tiger', 'giraffe', 'rhinoceros', 
              'bee', 'bull', 'fox', 'boar','zebra',
              'porcupine', 'cheetah','dog','cat', 'cow',
              'donkey','horse','snake', 'crocodile', 'spider',
              'rat','parrot', 'eagle','crow', 'vulture',
              'peacock','dove','sparrow','bee']
###################################################

wild = ['elephant', 'lion', 'tiger', 'giraffe', 'rhinoceros', 
        'bull', 'fox', 'boar','zebra', 'porcupine', 'cheetah',
        'eagle','crow', 'vulture','peacock']
###################################################
domestic = ['dog','cat', 'cow', 'donkey','horse','parrot']
###################################################
animal = list()
animal.extend(wild)
animal.extend(domestic)
###################################################
reptile = ['snake', 'crocodile', 'spider', 'rat']
###################################################
birds = ['parrot', 'eagle','crow', 'vulture','peacock',
              'dove','sparrow','bee']
###################################################
path = 'C:/Users/srama/OneDrive/Desktop/project 1'
img_path = path.join(str(name)+'.jpg')
###################################################
try:
    img = mpimg.imread(str(name)+'.jpg')
    plt.imshow(img)
except:
    print("\n \n I think , you should enter the correct spelling friend")
###################################################
height = ['2.8 - 3.2 meters','1.2 meters','70 – 120 cms','4.6 – 6.1 m','1.7 – 1.9 m',
          '39 millimetres','1.2 m ',8,9,10,
          11,12,13,14,15,
          16,17,18,19,20,
          21,22,23,24,25,
          26,27,28,29]

###################################################
Length = ['5.5 – 6.5 m','184–208 cm','2.5 – 3.9 m','4.2 m','2.8 -3.8 m',
          '15mm','2.2 m',8,9,10,
          11,12,13,14,15,
          16,17,18,19,20,
          21,22,23,24,25,
          26,27,28,29]
###################################################
weight = ['4,000 kg','Male: 190 kg (Adult), Female: 130 kg (Adult)','Male: 90 – 310 kg, Female: 65 – 170 kg', '800 kg','2,200 kg',
          ' 0.05 grams','640 – 900 kg',8,9,10,
          11,12,13,14,15,
          16,17,18,19,20,
          21,22,23,24,25,
          26,27,28,29]
###################################################
life_span = ['60 – 70 years','10 – 14 years','10 – 15 years','26 years','35 – 50 years',
             '122 – 152 days','18 – 22 years',8,9,10,
              11,12,13,14,15,
              16,17,18,19,20,
              21,22,23,24,25,
              26,27,28,29]
###################################################
region = ['Greenish','Moderate','Moderate','Africa','Greenish',
          'Greenish','universal',8,9,10,
          11,12,13,14,15,
          16,17,18,19,20,
          21,22,23,24,25,
          26,27,28,29]
###################################################
bot_name = ['Loxodonta','Panthera leo','Panthera tigris','Giraffa','Rhinocerotidae',
            'Anthophila',8,9,10,
          11,12,13,14,15,
          16,17,18,19,20,
          21,22,23,24,25,
          26,27,28,29]
###################################################
population = [500000,20000,3948,111000,27300,
              '90 million',7,8,9,10,
              11,12,13,14,15,
              16,17,18,19,20,
              21,22,23,24,25,
              26,27,28,29]
###################################################
index_dict = dict()
for i in enumerate(being_list):
    index_dict[i[1]] = i[0]
###################################################

###################################################

from tabulate import tabulate

col_1 = ['Type','SubType', 'Height','Weight', 'Life Span',
         'Region', 'Botanical Name','Population']

col_2= list()



if name in being_list:
    if name in animal:
        col_2.append('Animal')
    elif name in birds:
        col_2.append('Bird')
    else:
        col_2.append('Reptile')
        
        
if name in wild:
    col_2.append('Wild')
elif name in domestic:
    col_2.append( 'Domestic')
else:
    col_2.append('Universal')

try:
    id_num = index_dict[name]
except:
    print('ID error')


try:
        
    col_2.append(height[id_num])
    col_2.append(weight[id_num])
    col_2.append(life_span[id_num])
    col_2.append(region[id_num])
    col_2.append(bot_name[id_num])
    col_2.append(population[id_num])

except:
    print("check this please")
###################################################
print('\n \n')
table1 = zip(col_1,col_2)
headers1 = ['Specification','Details']
table = tabulate(table1,headers1)

print(table)



