#5210411211_Muhammad Rifqi Sahib

import cv2

# memuat gambar
img = cv2.imread('dog.jpeg')
print(img.shape) # print gambar awal sebelum diterapkan efek negatif
cv2.imshow('gambar awal', img)

# Invert gambar menggunakan cv2.bitwise_not
img_negativ = cv2.bitwise_not(img)

# tampilkan gambar yang sudah dinegatifkan
cv2.imshow('gambar negative', img_negativ)

# menekan tombol apapun akan menutup jendela
cv2.waitKey()