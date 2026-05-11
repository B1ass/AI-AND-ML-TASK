#5210411211_Muhammad Rifqi Sahib
import cv2
import numpy as np
   
# membaca gambar dengan perintah imread
image1 = cv2.imread('petir.jpg')
image2 = cv2.imread('gunung.jpg')

#memasukkan gambar dengan parameter yang diterapkan
weightedSum = cv2.addWeighted(image1, 0.1, image2, 0.9, 0)
 
# menampilkan operasi penjumlahan
cv2.imshow('hasil penjumlahan citra', weightedSum)
cv2.imshow('gambar awal petir',image1)
cv2.imshow('gambar awal gunung',image2)
 
# meng-alokasikan penggunaan memori
if cv2.waitKey() & 0xff == 27:
    cv2.destroyAllWindows()