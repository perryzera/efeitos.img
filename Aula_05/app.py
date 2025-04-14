import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem_nome = 'planta.png'

imagem = cv2.imread(imagem_nome, cv2.IMREAD_GRAYSCALE)

if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

prewitt_x = np.array([[-1, 0, 1],
                      [-1, 0, 1],
                      [-1, 0, 1]])

prewitt_y = np.array([[1, 1, 1],
                      [0, 0, 0],
                      [-1, -1, -1]])

prewitt_x_result = cv2.filter2D(imagem, -1, prewitt_x)
prewitt_y_result = cv2.filter2D(imagem, -1, prewitt_y)
prewitt_xy_result = cv2.addWeighted(prewitt_x_result, 0.5, prewitt_y_result, 0.5, 0)

def adicionar_texto(imagem, texto):
    imagem_colorida = cv2.cvtColor(imagem, cv2.COLOR_GRAY2BGR)
    cv2.putText(imagem_colorida, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 255, 0), 2, cv2.LINE_AA)
    return imagem_colorida

x_com_texto = adicionar_texto(prewitt_x_result, 'bordas verticais')
y_com_texto = adicionar_texto(prewitt_y_result, 'bordas horizontais')
xy_com_texto = adicionar_texto(prewitt_xy_result, 'todas as bordas')

plt.figure(figsize=(16, 5))
plt.subplot(1, 4, 1)
plt.imshow(original_com_texto[..., ::-1])
plt.title('Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(x_com_texto[..., ::-1])
plt.title('Prewitt X')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(y_com_texto[..., ::-1])
plt.title('Prewitt Y')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(xy_com_texto[..., ::-1])
plt.title('Prewitt XY')
plt.axis('off')

plt.tight_layout()
plt.show()
