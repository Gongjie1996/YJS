import cv2
import os

img_path = './Data/images/'
img_list = os.listdir(img_path)

full_img_path = []
img_p = []
for i in range(0, len(img_list)):
    path = img_path + img_list[i]
    full_img_path.append(path)
    img = cv2.imread(full_img_path[i], 1)
    img1 = img[0:960, 0:1280]
    img2 = img[960:1920, 0:1280]
    img3 = img[0:960, 1280:2560]
    img4 = img[960:1920, 1280:2560]
    list = [img1, img2, img3, img4]
    img_p.append(list)

print(len(img_p))

cv2.waitKey(0)
