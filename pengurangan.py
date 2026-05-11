#5210411211_Muhammad Rifqi Sahib
import cv2
import numpy as np
 
# fungsi imread untuk membaca gambar & fungsi imshow untuk menampilkan gambar
image = cv2.imread('dinosaurus.jpeg')
cv2.imshow('gambar awal', image)
 
# memperkecil gambar sehingga terbentuk lebar & tinggi baru
down_width = 100
down_height = 150
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
 
# meningkatkan gambar menggunakan lebar dan tinggi baru
up_width = 500
up_height = 300
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
 
# menampilkan gambar 
cv2.imshow('pengubahan ukuran ke bawah', resized_down)
cv2.waitKey()
cv2.imshow('pengubahan ukuran ke atas', resized_up)

# menekan tombol apapun akan menutup jendela
cv2.waitKey()
cv2.destroyAllWindows()