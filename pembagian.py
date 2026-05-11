#5210411211_Muhammad Rifqi Sahib
import cv2  
img = cv2.imread('brontosaurus.jpeg')
  
# cv2.imread() -> pengambilan gambar sebagai input
a, b, channels = img.shape
  
# membagi bagian kiri dan kanan
half = a//2

# gambar menjadi setengah atau terbagi menjadi dua gambar
bagian_kiri = img [:, :half] 
bagian_kanan = img [:, half:]  

# menampilkan gambar bagian kiri & bagian kanan
cv2.imshow('bagian kiri', bagian_kiri)
cv2.imshow('bagian kanan', bagian_kanan)
  
# membagi gambar atas dan bawah
half2 = b//2
  
# gambar menjadi setengah atau terbagi menjadi dua gambar
atas = img [:half2, :]
bawah = img [half2:, :]

# menampilkan gambar atas & bawah
cv2.imshow('bagian atas', atas )
cv2.imshow('bagian bawah', bawah)

# menekan tombol apapun akan menutup jendela
cv2.waitKey()