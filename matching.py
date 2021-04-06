
import _pickle as cPickle
import numpy as np
import cv2
import pysift
from matplotlib import pyplot as plt
import logging
import os
logger = logging.getLogger(__name__)

MIN_MATCH_COUNT = 20
kp_name = []
match = []

def kpmatching(des1,des2,image_name):
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Lowe's ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        match.append(image_name)

    return match





#img1 = cv2.imread('flower.jpg', 0)
#img2 = cv2.imread('14.jpg', 0)


#kp1, des1 = pysift.computeKeypointsAndDescriptors(img1)
#kp2, des2 = pysift.computeKeypointsAndDescriptors(img2)


des1 = np.loadtxt("KP/Faces_easy_image_0001.txt").astype('float32')




#print(des1)
#print(len(des1))

with os.scandir('KP') as entries:
    for entry in entries:
        # print(entry.name)
        kp_name.append(entry.name)

for i in kp_name:
    good=[]
    des2 = np.loadtxt("KP/" + str(i)).astype('float32')
    matches = kpmatching(des1,des2,i)


print(matches)


"""
#print(len(good))
if len(good) > MIN_MATCH_COUNT:
    print("Match Found with " + str(len(good)) + " Matches")

else:
    print("Not enough matches are found. Total matches found are: " + str(len(good)) + " Minimum match count is: " + str(MIN_MATCH_COUNT)  )
"""



"""
if len(good) > MIN_MATCH_COUNT:
    # Estimate homography between template and scene
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)[0]

    # Draw detected template in scene image
    h, w = img1.shape
    pts = np.float32([[0, 0],
                      [0, h - 1],
                      [w - 1, h - 1],
                      [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)

    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

    h1, w1 = img1.shape
    h2, w2 = img2.shape
    nWidth = w1 + w2
    nHeight = max(h1, h2)
    hdif = int((h2 - h1) / 2)
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)

    for i in range(3):
        newimg[hdif:hdif + h1, :w1, i] = img1
        newimg[:h2, w1:w1 + w2, i] = img2

    # Draw SIFT keypoint matches
    for m in good:
        pt1 = (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1] + hdif))
        pt2 = (int(kp2[m.trainIdx].pt[0] + w1), int(kp2[m.trainIdx].pt[1]))
        cv2.line(newimg, pt1, pt2, (255, 0, 0))

    plt.imshow(newimg)
    plt.show()
else:
    print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))


"""



















"""
im=cv2.imread("flower.jpg")

index = cPickle.loads(open("keypoints.txt").read())



kp = []

for point in index:
    temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2],
                            _response=point[3], _octave=point[4], _class_id=point[5])
    kp.append(temp)

# Draw the keypoints
imm=cv2.drawKeypoints(im, kp);
cv2.imshow("Image", imm);
cv2.waitKey(0)
"""