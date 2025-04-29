import cv2
import numpy as np

image01 = cv2.imread('zmg01.png', cv2.IMREAD_GRAYSCALE)
image02 = cv2.imread('zmg02.jpg', cv2.IMREAD_GRAYSCALE)
image03 = cv2.imread('zmg03.jpg', cv2.IMREAD_GRAYSCALE)

cantos01 = cv2.goodFeaturesToTrack(
    image01,
    maxCorners= 100,
    qualityLevel= 0.04,
    minDistance= 10
)
cantos02 = cv2.goodFeaturesToTrack(
    image02,
    maxCorners= 150,
    qualityLevel= 0.1,
    minDistance= 4
)
cantos03 = cv2.goodFeaturesToTrack (
    image03,
    maxCorners= 190,
    qualityLevel= 0.2, 
    minDistance= 6
)

cantos01 = np.int64(cantos01)
cantos02 = np.int64(cantos02)
cantos03 = np.int64(cantos03)

# maxCorner     => número máximo de cantos a detectar
# qualityLevel  => valores mínimos aceitáveis para min(L1, L2)
# minDistance   => distância mínima entre dois cantos

# Marcar cantos na imagem
for canto01 in cantos01 :
    x, y = canto01.ravel()
    cv2.circle(image01, (x, y), 3, 255, -1)

for canto02 in cantos02 :
    x, y = canto02.ravel()
    cv2.circle(image02, (x, y), 3, 255, -1)

for canto03 in cantos03 :
    x, y = canto03.ravel()
    cv2.circle(image03, (x, y), 3, 255, -1)

# Exibir resultados
cv2.imshow('Resultado 01 Shi-Tomasi: ', image01)
cv2.imshow('Resultado 02 Shi-Tomasi: ', image02)
cv2.imshow('Resultado 03 Shi-Tomasi: ', image03)

cv2.waitKey(0)
cv2.destroyAllWindows()