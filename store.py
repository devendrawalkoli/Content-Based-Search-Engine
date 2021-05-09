import cv2
import pysift
import numpy as np
import os
import time

# creating dataset

cat = []
data = []

with os.scandir('dataset') as entries:
    for entry in entries:
        # print(entry.name)
        cat.append(entry.name)

for i in range(0, len(cat)):
    data.append([])
    with os.scandir('dataset/' + str(cat[i])) as entries:
        for k in entries:
            data[i].append(k)

# DirEntry to string conversion

sp = (data[0][0])
new = str(sp)
new = new[:-2]
new = new[-14:]

# print(new)

str1 = ""
str2 = ""
path = ""
a = 0
t = 3294
d = 0

start = time.time()
for i in data:
    str1 = cat[a]
    a = a + 1
    for j in i:
        sp = (j)
        str2 = str(sp)
        str2 = str2[:-2]
        str2 = str2[-14:]
        str3 = str2[:-4]

        # data storing
        new_path = "KP/" + str(str1) + "/"

        img = cv2.imread('dataset/' + str1 + '/' + str2, 0)
        kp1, des1 = pysift.computeKeypointsAndDescriptors(img)
        np.savetxt(new_path + "_" + str3 + ".txt", des1)
        t = t - 1
        d = d + 1
        end = time.time()
        elapsed_time = end - start
        print(str1 + "   " + str2 + " Done...  " + str(t) + " Remain...." + " Images Done: "+ str(d) + " Elapsed Time: "
              + str(int(elapsed_time)) + "sec  " + "Keypoint count: " + str(len(kp1)))
















"""

image = cv2.imread('flower.jpg', 0)
keypoints, descriptors = pysift.computeKeypointsAndDescriptors(image)

kp = []
kp = keypoints
ds = []
ds = descriptors

print(kp)

index = []
for point in kp:
    temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id)
    index.append(temp)

# Dumping of keypoints
f = open("keypoints.txt", "wb")
f.write(cPickle.dumps(index))
f.close()


"""

"""
f2 = open("dis.txt", "wb")
f2.write(ds)
f2.close()

"""
