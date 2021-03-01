
import cv2
import pysift
import _pickle as cPickle


image = cv2.imread('flower.jpg', 0)
keypoints, descriptors = pysift.computeKeypointsAndDescriptors(image)

kp = []
kp = keypoints
#print(kp)

index = []
for point in kp:
    temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id)
    index.append(temp)

# Dump the keypoints
f = open("keypoints.txt", "wb")
f.write(cPickle.dumps(index))
f.close()



