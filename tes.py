def labeling(imgID):
	id = imgID[0:imgID.find('.jpg')]
	
	if len(id) <= 2:
		return 0
	if len(id) == 3:
		return id[0]
'''
str1 = 'dataset\\99.jpg'
str2 = str1[str1.find("\\") + 1:]

print str1
print str2[0]

i = 1
t = 'Result {}'.format(i)
print t

nama = str2[0:str2.find('.jpg')]
print '>>> ', nama

if len(nama) <= 2:	
	print 'class 1'

if len(nama) == 3:
	print 'class ', nama[0]

print 'class == ', labeling(nama)
	
#0-99: people
#100-199: beach
#200-299: building
#300-399: bus
#400-499: dinosaur
#500-599: elephant
#600-699: flower
#700-799: horse
#800-899: mountain
#900-999: food

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

# Take Red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

plt.show()

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.KNearest()
knn.train(trainData,responses)
ret, results, neighbours ,dist = knn.find_nearest(newcomer, 3)

# 10 new comers
newcomers = np.random.randint(0,100,(10,2)).astype(np.float32)
ret, results,neighbours,dist = knn.find_nearest(newcomer, 3)
# The results also will contain 10 labels.

print "result: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist

plt.show()

result = [(4.5113858810175476, '34_ferrari_308gts_1979_side.jpg'), (8.1150574673278442, '42_ferrari_f430_2005_side.jpg'), (8.1369157450254832, '34_ferrari_308gts_1979_rear.jpg'), (8.8411715153251613, '39_ferrari_f40_1990_side.jpg'), (9.1198334438072148, '40_ferrari_f50_1995_side.jpg'), (9.1269109657066583, '35_ferrari_360_spider_2001_side.jpg'), (10.373858151665818, '35_ferrari_360_spider_2001_rear.jpg'), (10.418366835693362, '42_ferrari_f430_2005_rear.jpg'), (10.567626595301526, '37_ferrari_550_barchetta_2001_rear.jpg'), (10.592533005293955, '88_mercedes_benz_190e_evolution_2_1990_side.jpg')]

import csv

idx = []
for (score,image) in result:
	id = int(image[:image.find("_")])
	idx.append(id)

print 34 in idx

# initialize our dictionary of results
info_results = {}

# open the index file for reading
with open("infocar.csv") as f:
	# initialize the CSV reader
	reader = csv.reader(f)
	
	for row in reader:
		if int(row[0]) in idx:
			info_results[int(row[0])] = row[1:]
	
	f.close()

info = info_results[88]
print "Info Car: \n name: ",info[0],"\n Type: ",info[1],"\n Price: ",info[2],"\n Year: ",info[3],"\n Maker: ",info[4],"\n Country: ",info[5]

print info_results," len: ",len(info_results)
print idx," len: ",len(idx)

import os
import math
import random
import copy
import numpy as np
from numpy import array
#from img_hash import EXTS

def norm0_dist(h1, h2):
    return len(h1) - sum(array(h1)==array(h2))    

def eculidean_dist(h1, h2):
    return math.sqrt(square_eculidean_dist(h1, h2))

def square_eculidean_dist(h1, h2):
    return sum((array(h1)-array(h2))**2)

def kmeans_classify(centers, h):
    min_c, min_d = -1, -1
    for c, center in enumerate(centers):
        d = square_eculidean_dist(h, center)
        if min_c == -1 or d < min_d:
            min_c, min_d = c, d
    return min_c

def save_centers(p_out, centers):
    with open(p_out, 'w') as fout:
        for center in centers:
            fout.write('%s\n' % (repr(center)))

def load_centers(p_center):
    centers = [] 
    for line in open(p_center):
        centers.append(eval(line.strip()))
    return centers

def kmeans(p_feat, p_out, nclass=100, max_iter=100, percent=0.02, theta=0.01):
    feat_list = [] 
    for line in open(p_feat):
        if random.random() <= percent:
            arr = line.strip().split('\t')
            path, feat = arr[0], eval(arr[1])
            feat_list.append(feat)
    print 'feat_list len', len(feat_list)
    print 'feat len', len(feat_list[0]) 

    theta2 = nclass * 100. / len(feat_list)
    print 'theta2', theta2

    centers = random.sample(feat_list, nclass)
    for niter in range(max_iter): 
        print 'iter %d...' % niter
        old_centers = copy.deepcopy(centers)
        print 'old_centers finished'
        class_feats = [[] for i in range(len(centers))]
        print 'class_feats initialized'
        for feat in feat_list:
            if random.random() < theta2: 
                min_c = kmeans_classify(centers, feat)
                class_feats[min_c].append(feat)
        print 'class_feats finished'

        centers = []
        for i, feats in enumerate(class_feats):
            if feats:
                centers.append(list(np.mean(feats, 0)))
            else:
                centers.append([0]*len(feat_list[0]))
        print 'centers finished, len:', len(centers)

        save_centers(p_out, centers)
        print 'saved centers...'

        diff = 0
        for c, center in enumerate(centers):
            diff += eculidean_dist(center, old_centers[c])
        print 'diff %s', diff
        if diff < theta:
            break

def test():
    a = [[1, 2], [5,6]]
    b = [1.5, 3]
    c = kmeans_classify(a, b)
    print a, b, c


if __name__ == '__main__':
    test()
'''
from module.clustering import Clustering
import cv2
import numpy

K = 10
C = Clustering(K)

image = cv2.imread('queries/q5.jpg')
new_img = C.color_quantization_kmeans(image)
features = C.cal_region_hist(new_img)

print 'Number of Clustering: ', K
print 'Features:\n', features, '\n Len(features): ', len(features),'\n Unique Features:\n', numpy.unique(features)
print '\n len(unique features): \n', len(numpy.unique(features))

cv2.imshow('Original', image)
cv2.imshow('Result', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()