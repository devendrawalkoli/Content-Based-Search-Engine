# import _pickle as cPickle
import numpy as np
import cv2
import pysift
# from matplotlib import pyplot as plt
import logging
import os
import time
# import multiprocessing as mp
# from numba import jit, njit
import numpy as np

import multiprocessing
from itertools import product

logger = logging.getLogger(__name__)

# MIN_MATCH_COUNT = 8
kp_name = []
match = []
matches = []


def kpmatching(des1, des2, image_name, MIN_MATCH_COUNT, path):
    global matches
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    try:
        matches = flann.knnMatch(des1, des2, k=2)
    except:
        pass

    MIN_MATCH = MIN_MATCH_COUNT

    # Lowe's ratio test

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    path = path.replace("KP", "dataset")

    print("Good: " + str(len(good)))

    if len(good) > MIN_MATCH:
        match.append(path + image_name)

    return match


def match_main(des, img_label):
    t0 = time.time()

    # des1 = np.loadtxt("KP/" + str(des)).astype('float32')
    t2 = time.time()
    img = cv2.imread(des, 0)
    kp1, des1 = pysift.computeKeypointsAndDescriptors(img)
    print(" Key-points Found: " + str(len(des1)))
    match_found = 0
    t3 = time.time() - t2
    print("Time for KP extraction: " + str(t3))
    path = "KP/" + str(img_label) + "/"
    path2 = "KP/" + str(img_label)
    kp_name.clear()
    with os.scandir(path2) as entries:
        for entry in entries:
            # print(entry.name)
            kp_name.append(entry.name)

    # print(kp_name)

    min_match = len(des1)
    if min_match < 10:
        min_match = len(des1) - 1
    else:
        min_match = 8

    print("KP name: ")
    print(kp_name)

    for i in kp_name:
        file_size = os.path.getsize(path + str(i))
        if file_size == 0:
            pass
        else:
            des2 = np.loadtxt(path + str(i)).astype('float32')
            match_found = kpmatching(des1, des2, i, min_match, path)

    print(" Matched Images: " + str(match_found))
    t1 = time.time() - t0
    print("Time for KP Matching: " + str(t1))
    return match_found


"""""
    else:
        for i in range(len(folder_name)):
            path = "KP/" + str(folder_name[i]) + "/"
            path2 = "KP/" + str(folder_name[i])
            with os.scandir(path2) as entries:
                for entry in entries:
                    print(entry.name)
                    kp_name.append(entry.name)

            for j in kp_name:
                good = []

                des2 = np.loadtxt(path + str(j)).astype('float32')
                match_found = kpmatching(des1, des2, i, len(des1))

            return match_found
"""

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
