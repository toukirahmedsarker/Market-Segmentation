import random as rand
from kmclustering import clustering
from point import Point
import csv

geo_locs = []
 

f = open('C:\\Users\\TOUKIR\\Desktop\\class\\New folder (2)\\New folder\\data-mining\\data mining_\\example.csv', 'r')
reader = csv.reader(f, delimiter=",")


for line in reader:
        #loc_ = Point(float(line[0]), float(line[1]),str(line[3])) #tuples for location
        loc_ = Point(float(line[0]), float(line[1]))
        geo_locs.append(loc_)

 

cluster = clustering(geo_locs,4) #cluster is object of clustering

flag = cluster.k_means(True)

if flag == -1:
    print ("Error in arguments!")
