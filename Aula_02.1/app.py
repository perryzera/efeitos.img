import cv2
import numpy as np

BREAK_EXECUTION_OF_CODE = 0
DEFINE_SAME_DEEP_ORIGINAL_IMAGE = -1

image_rgb = cv2.imread(r"C:\Users\perry\Documents\Facul\7 SEM\VisaoComputacional\Aula_02.1\planta.png", cv2.IMREAD_COLOR)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

def show_images(originalImage, chandegImage, cv2):
    cv2.imshow("Original", originalImage)
    cv2.imshow("Modificada", chandegImage)
    cv2.waitKey(BREAK_EXECUTION_OF_CODE)
    cv2.destroyAllWindows()


#cv2.filter2D (src, ddepth, kernel, ...)
# src -> faz referencia a imagem de entrada
# ddepth -> Profundidade da imagem de saida, quando ela recebe
# -1, a profundidade de saída se mantém igual a de entrada
# kernel -> define a operação de convolução

# convolução -> um deslizamento de um pequeno kernel(ou mascara)
# na imagem principal
# cada pixel da imagem é submetido a uma soma ponderada com o kernel
# isso resulta em efeitos como "suavização, realce, e boras
# detectação de contorno, entre outros"

'''
image_sharped = cv2.filter2D(
    image_rgb,
    DEFINE_SAME_DEEP_ORIGINAL_IMAGE,
    kernel
)
show_images(
    image_rgb,
    image_sharped,
    cv2
)
'''

## Equalização ded Histograma
image_cinza = cv2.imread(
    './planta/png',
    cv2.IMREAD_GRAYSCALE
)
image_eq = cv2.equalizeHist(image_cinza)

# show_images(image_cinza, image_eq, cv2)


# REDIRECIONAMENTO DE IMAGENS
# (altera o tamanho)
image_rend = cv2.resize(image_rgb, (300,500))

#show_images(
#    image_rgb,
#    image_rend,
#    cv2
#)

# ROTACIONAR IMAGENS

(h, w) = image_rgb.shape[:2]
centro = (w / 2, h /2)

# função getRotationMatrix2D utilizada para fazer
# rotação em duas dimensões
# cv2.getRotationMatrix2D(center, angle, scale)
# center -> é o centro da imagem
# angle -> é o ângulo em graus
# scale -> fator de escalagem da imagem, 1 mantem a imagem no tamanho
# normal 

# retorno da função é uma matriz M 2x3 
# que pode ser aplicada a função warpAffine

matriz_rotacao = cv2.getRotationMatrix2D(
    centro,
    45,
    1.0
)

print("Matriz Rotação")
print(matriz_rotacao)

image_rotation = cv2.warpAffine(
    image_rgb,
    matriz_rotacao,
    (h, h)
)

show_images(
    image_rgb,
    image_rotation,
    cv2
)

