import cv2
import numpy as np

image01 = cv2.imread('planta.png', cv2.IMREAD_GRAYSCALE)
image02 = cv2.imread('cr7.jpg', cv2.IMREAD_GRAYSCALE)
image03 = cv2.imread('ronaldos.jpg', cv2.IMREAD_GRAYSCALE)

# Algoritmo usado para detectar cantos - detecção ocorre com uma mudança de pixel em múltiplas direções

# blockSize => tamanho do vizinho considerado pela detecção do canto
# ksize     => tamanho da abertura do sobel para derivadas parâmetro livre para esq. de Harris
# k         => parâmetro livre da equação de Harris

harris01 = cv2.cornerHarris(image01, blockSize=2, ksize=3, k=0.04)
harris02 = cv2.cornerHarris(image02, blockSize=3, ksize=1, k=0.1)
harris03 = cv2.cornerHarris(image03, blockSize=4, ksize=5, k=0.2)

dist01 = cv2.dilate(harris01, None)
dist02 = cv2.dilate(harris02, None)
dist03 = cv2.dilate(harris03, None)

# Destacar os cantos na imagem original
image01[harris01 > 0.01 * harris01.max()] = [255]
image02[harris02 > 0.01 * harris02.max()] = [255]
image03[harris03 > 0.01 * harris03.max()] = [255]

# Exibir Resultados 01
cv2.imshow('Resultado 01', image01)
cv2.imshow('Resoltado 02', image02)
cv2.imshow('Resultado 03', image03)
cv2.waitKey(0)
cv2.destroyAllWindows()