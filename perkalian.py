#5210411211_Muhammad Rifqi Sahib
import cv2
import numpy as np

# membaca gambar dengan perintah imread
img1 = cv2.imread('gunung.jpg')
img2 = cv2.imread('petir.jpg')

result_image = cv2.multiply(img1, img2)
cv2.imshow('hasil perkalian citra', result_image)

# menekan tombol apapun akan menutup jendela
cv2.waitKey()
cv2.destroyAllWindows()