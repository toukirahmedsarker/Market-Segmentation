import random as rand
import math as math
from point import Point 

class clustering:
    def __init__(self, geo_locs_, k_):
        self.geo_locations = geo_locs_
        self.k = k_
        self.clusters = {} #clusters of nodes
        self.centroids = []#centroids
        self.maxIter = 11

    #this method returns the next random node
    def next_random(self, index, points, clusters):

        #pick next node that has the maximum distance from other nodes
        dist = {}
        for point_1 in points:
            for cluster in clusters.values():
                point_2 = cluster[0]
                if point_1 not in dist:
                    dist[point_1] = math.sqrt(math.pow(point_1.latit - point_2.latit,2.0) + math.pow(point_1.longit - point_2.longit,2.0))
                else:
                    dist[point_1] += math.sqrt(math.pow(point_1.latit - point_2.latit,2.0) + math.pow(point_1.longit - point_2.longit,2.0))

        count_ = 0
        max_ = 0
        for key, value in dist.items():
            if count_ == 0:
                max_ = value
                max_point = key
                count_ += 1
            else:
                if value > max_:
                    max_ = value
                    max_point = key
        return max_point

    def print_clusters(self, clusters):
        cluster_cnt = 1
        for cluster in clusters.values():
            print ("nodes in cluster #%d" % cluster_cnt)
            cluster_cnt += 1
            for point in cluster:
                print ("point(%f,%f)" % (point.latit, point.longit))


    def initialize_centroid(self,points):

        point_ = rand.choice(points)
        centroid = dict()
        centroid.setdefault(0, []).append(point_) #add point_ to cluster dictionary
        points.remove(point_)

        for i in range(1, self.k):
            point_ = self.next_random(i, points, centroid)
            centroid.setdefault(i, []).append(point_)
            points.remove(point_)

       # self.print_clusters(centroid)
        for cluster in centroid.values():
            for point_ in cluster:
                self.centroids.append(point_)
        self.clusters = centroid.copy()




    def assign_points(self,points,flag):
        #self.print_clusters(self.clusters)
        if flag==1 :
            self.clusters.clear()
        index = 1
        for point_cen in self.centroids:
             print ("(%f,%f%s %d)" % ( point_cen.latit, point_cen.longit," : centroids",index))#print centroids
             index+=1
        for point_ in points:
            id = 0
            min_id = 0
            min_dis = 0
            for point_cen in self.centroids:
                #print "(%d,%f,%f)" % (id,point_cen.latit, point_cen.longit)
                dis = math.sqrt(math.pow(point_.latit - point_cen.latit,2.0) + math.pow(point_.longit - point_cen.longit,2.0))
                #print dis
                if id==0:
                    min_dis = dis
                    min_id = id

                else:
                    if dis<min_dis:
                        min_dis = dis
                        min_id = id
                id += 1
            self.clusters.setdefault(min_id,[]).append(point_)

        #self.print_clusters(self.clusters)
    ''' i = 0
        for point in self.centroids:
            self.clusters.setdefault(i,[]).append(point)
            #print "(%f,%f)" % (point.latit, point.longit)
            i += 1'''

    def update_centroid(self):

        size =  len(self.centroids)
        # print size
        # print len(self.clusters)
        for i in range(0,size,1):
            point = self.centroids.pop()

        for point_cen in self.centroids:
            print ("(%f,%f%s)" % ( point_cen.latit, point_cen.longit,"toukir"))#nothing to be print

        for clusters in self.clusters.values():
            cnt = 0
            sum_latit = 0.0
            sum_longit = 0.0
            for point in clusters:
                sum_latit = sum_latit+point.latit
                sum_longit = sum_longit+point.longit
                cnt += 1
           # loc_ = Point(float(sum_latit/cnt), float(sum_longit/cnt),str("toha"))
                loc_ = Point(float(sum_latit / cnt), float(sum_longit / cnt))
            self.centroids.append(loc_)


    #k_means algorithm
    def k_means(self, plot_flag):
        if len(self.geo_locations) < self.k: #if num of locations are less than clusters then error
            return -1   #error

        points_ = [point for point in self.geo_locations]

        self.initialize_centroid(points_)
        self.assign_points(points_,0)
        #self.plot_figure(True,self.clusters,0)
        self.print_clusters(self.clusters)
        points_ = [point for point in self.geo_locations]
        for i in range(1,20,1):
            self.update_centroid()
            self.assign_points(points_,1)
            #self.plot_figure(True,self.clusters,i)
            self.print_clusters(self.clusters)
        return 0

        # plot_figure
     
