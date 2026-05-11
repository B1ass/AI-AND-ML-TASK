import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

citra = cv2.imread("Latihan - pekan 10.jpg", cv2.IMREAD_UNCHANGED)

scale_percent = 20

width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
hasil = cv2.resize(citra, dsize)

# 1. Rotasi 5 derajat berlawanan jarum jam
rotasi = imutils.rotate(hasil, 5)

# 2. Meningkatkan brighhtness
alpha = 2 # simle contrass control 
beta = 50 # simple brightness control

cerah = cv2.addWeighted(rotasi, alpha, np.zeros(rotasi.shape, rotasi.dtype), 0, beta)

# 3. Mempertajam gambar
kernel = np.array([ [-1, -1, -1],
                  [-1, 9, -1],
                  [-1, -1, -1]])

tajam = cv2.filter2D(cerah, -1, kernel)

cv2.imshow("Result", tajam)
cv2.waitKey()