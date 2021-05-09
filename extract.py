import cv2
import pysift
import _pickle as cPickle
import numpy as np
import time


start = time.time()

img = cv2.imread('dataset/image_0023.jpg', 0)

kp1, des1 = pysift.computeKeypointsAndDescriptors(img)

print("KPS: ")
print(len(kp1))
print("DCS: ")
print(len(des1))

end = time.time()

Time = end - start

print("Time: " + str(Time))

"""""
new = np.loadtxt("dis.txt").astype('float32')
print(new)

"""

"""
im=cv2.imread("flower.jpg")

index = cPickle.loads(open("keypoints.txt").read())

kp = []

for point in index:
    temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2],_response=point[3], _octave=point[4], _class_id=point[5])

    kp.append(temp)

# Draw the keypoints
imm=cv2.drawKeypoints(im, kp);
cv2.imshow("Image", imm);
cv2.waitKey(0)


"""