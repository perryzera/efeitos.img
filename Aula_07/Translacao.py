import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('C:\\Users\\JOAOVITORPERRYTULIO\\Documents\\efeitos.img-main\\Aula_07\\planta.png')

# Definir a matriz de translação
tx, ty = 100, 50
matriz_translacao = np.float32([[1, 0, tx], [0, 1, ty]])

# Aplicar a translação
imagem_transladada = cv2.warpAffine(imagem, matriz_translacao, (imagem.shape[1], imagem.shape[0]))

# Exibir resultado
cv2.imshow('Imagem Transladada', imagem_transladada)
cv2.waitKey(0)
cv2.destroyAllWindows()
