import math

import numpy as np

from config import Config


class KalmanFilter():

    def __init__(self):
        updateFrequency = 1
        self.q = np.diag([0.002, 0.002, 0.0005, 0.0005])
        self.x = np.array([[0.01, 0.01, 0.01, 0.1]]).transpose()
        self.p = np.diag([1000000, 1000000, 1000000, 1000000])
        self.i = np.diag([1., 1., 1., 1.])
        self.a = np.array([[1, 0, updateFrequency, 0], [0, 1, 0, updateFrequency], [0, 0, 1, 0], [0, 0, 0, 1]],
                          dtype=float)
        self.er = np.array([[0,0,0,0]],dtype=float)
        self.distances_buffer = {}
        self.distances_buffer_counter = {}
        self.distances_volt = 0


    def inner_update(self, distances):

        z = []
        meaningless_h = []
        r = np.diag([200, 200, 200, 200])
        h = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]])
        self.x =self.a.dot(self.x)
        self.p = self.a.dot(self.p).dot(self.a.transpose())+self.q

        for (key,distance) in distances.items():
            anchor = Config.anchors[str(key)]
            temp = (math.pow(self.x[0][0] - anchor[0], 2) + math.pow(self.x[1][0] - anchor[1], 2))
            meaningless_h.append(distances[key] * distances[key] - temp);
            h1 = (self.x[0][0] - anchor[0]) * 2
            h2 = (self.x[1][0] - anchor[1]) * 2
            h[key-1][0]=h1
            h[key-1][1]=h2


            # if self.er[0][key-1]>1:
            # r[key-1][key-1]=self.er[0][key-1]*self.er[0][key-1]
            #     if distance < 5:
            #         r[key-1][key-1]=0.1*distance
            # else:
            #     r[key-1][key-1]=0.15
            # z.append(distance)

        dominate = np.mat(h.dot(self.p).dot(h.transpose()) + r)

        k = self.p.dot(h.transpose()).dot(dominate.I)



        # self.mz = np.array([z]).transpose()
        # meaningless_h.append(self.x[3][0])
        # meaningless_h.append(self.x[4][0])
        # meaningless_h.append(self.x[5][0])
        self.mh = np.array([meaningless_h]).transpose()
        self.x = self.x + k.dot(self.mh)
        self.p =(self.i - k.dot(h)).dot(self.p)

        return (float(self.x[0][0]), float(self.x[1][0]))

    def update(self, anchorId, distance):
        # Init
        if len(self.distances_buffer) == 0:
            for anchor_key in Config.anchors:
                self.distances_buffer[int(anchor_key)] = 0
                self.distances_buffer_counter[int(anchor_key)] = 0
        # Assign
        for item in self.distances_buffer_counter:
            temp = self.distances_buffer_counter[item]
            self.distances_buffer_counter[item] = temp + 1
            if temp > 5000:
                #self.distances_buffer[temp] = 0.0
                #logging.warning("Unable to receive node:%d"%item)
                pass
        # lastDistance = self.distances_buffer[anchorId];
        # if (math.fabs(distance-lastDistance)<2):
        #     self.distances_buffer[anchorId] = distance
        # else:
        #
        #     self.distances_buffer[anchorId] = lastDistance + 2;
        self.distances_buffer_counter[anchorId] = 0
        self.distances_buffer[anchorId] = distance

        self.distances_volt += 1
        if self.distances_volt > 2:
            self.distances_volt = 0
            result = self.inner_update(self.distances_buffer)
            # result = self.likelihood_reweight(self.distances_buffer)
            # for item in self.distances_buffer:
            #     self.distances_buffer[item] = 0
            return result
        #logging.warning("N")
        return None


# Config.load_config()
# filter = KalmanFilter()
#
# i = 0
# x = 0
# y = 0
# distance={}
# time = 5000
# totalerror = 0
# sign = 1
# while i < time:
# x += 0.1*sign
#     y += 0.1*sign
#     if(x>=4):
#         sign = -1;
#     if(x<=0):
#         sign = 1;
#
#     for key in Config.anchors:
#         item = Config.anchors[key]
#         distance[int(key)] = math.sqrt((x-item[0])**2+(y-item[1])**2)+np.random.normal(loc=0.0, scale=3, size=None)
#
#
#
#     result = filter.update(distance)
#     x1 = result[0]
#     y1 = result[1]
#     error = (x-x1)**2 + (y-y1)**2
#     totalerror+=error
#     print("realposition: %f %f calcposition %f %f error:%f" % (x,y,x1,y1,error))
#     i += 1
# print("Error:%f"%(totalerror/time))
