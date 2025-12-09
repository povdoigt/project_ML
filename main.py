import pandas as pd
from PIL import Image
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
import csv
import keras    

lettres = ['A','B','F','G','H','J','K','L']
lettres1 = ['A','B','F','G']
lettres2 = ['A','B','H','J']
lettres3 = ['A','F','H','K']
sides = 512

"""
fichiers = os.listdir('./lettres')
datas = []
for i in fichiers:
    docs = os.listdir(f'./lettres/{i}')
    for j in docs :
        datas.append(f'./lettres/{i}/{j}')

print(datas)"""


def resizer(img):
    L = []
    for i in range(0,512,64):   
        for j in range (0,512,64):
            L.append(img.crop((i,j,i+64,j+64)))
    return L



def get_points(sides,img): 
    points = pd.DataFrame(columns=['x', 'y'])
    for i in range(sides):
        for j in range(sides):
            if img.getpixel((i, j)) == 0:
                points.loc[len(points)] = [i, 63 - j]
    return points

def regression(points):

    X = points[['x']]
    if X.shape[0] == 0:
        return 0
    Y = points[['y']]

    regr = linear_model.LinearRegression()

    regr.fit(X, Y)

    print("Coefficients: \n", regr.coef_)

    return float(regr.coef_.ravel()[0])

def writing_csv(data, nom_csv):
    with open(nom_csv, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def lettre_bin(lettre):
    ajout = []
    if lettre in lettres1:
        ajout.append(0)
    else:
        ajout.append(1)
    if lettre in lettres2:
        ajout.append(0)
    else:
        ajout.append(1)
    if lettre in lettres3:
        ajout.append(0)
    else:
        ajout.append(1)
    return ajout



nom_csv = 'result.csv'
"""
for img in L:
    points = get_points(64)
    all_coefs.append(regression(points))
    writing_csv(all_coefs,csv)"""
"""
for images in datas:
    img =Image.open(images).convert('L')
    L = resizer(img)
    all_coefs= [] 
    for img in L:
        points = get_points(64,img)
        a = regression(points)
        b = (2*a)/(1+a**2)
        c = (1-a**2)/(1+a**2)
        all_coefs.append(b)
        all_coefs.append(c)
    if images[10] in lettres:
        all_coefs += lettre_bin(images[10])
    else:
        all_coefs += lettre_bin(images[12])
    writing_csv(all_coefs,nom_csv)
"""
"""
images = './lettres/O/B10.png'
img =Image.open(images).convert('L')
L = resizer(img)
all_coefs= [] 
for img in L:
    points = get_points(64,img)
    a = regression(points)
    a = (2*a)/(1+a**2)
    b = (1-a**2)/(1+a**2)
    all_coefs.append(a)
    all_coefs.append(b)
if images[10] in lettres:
    all_coefs += lettre_bin(images[10])
else:
    all_coefs += lettre_bin(images[12])
print(all_coefs)
print(len(all_coefs))
"""

image = './test_droite_64.png'
img = Image.open(image).convert('L')
print(get_points(64,img))



