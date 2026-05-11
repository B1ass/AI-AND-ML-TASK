#5210411211_Muhammad Rifqi Sahib
import cv2
import numpy as np
 
img = cv2.imread('anky.jpeg')
print(img.shape) # print gambar awal sebelum dipotong
cv2.imshow('gambar awal', img)
 
# melakukan pemotongan gambar
crop_image = img[30:400, 150:400]
 
# menampilkan gambar yang dipotong
cv2.imshow('crop gambar', crop_image)  

# menekan tombol apapun akan menutup jendela
cv2.waitKey()
cv2.destroyAllWindows()