import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread(r'C:\Users\JOAOVITORPERRYTULIO\Documents\efeitos.img-main\Aula_07\planta.png')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro: imagem não encontrada. Verifique o caminho ou o nome do arquivo.")
    exit()

# Definir os pontos de origem e destino
pts_origem = np.float32([[50, 50], [400, 50], [50, 400], [400, 400]])
pts_destino = np.float32([[110, 50], [315, 50], [50, 350], [320, 350]])

# Calcular a matriz de transformação perspectiva
matriz_perspectiva = cv2.getPerspectiveTransform(pts_origem, pts_destino)

# Obter dimensões da imagem original
h, w = imagem.shape[:2]

# Aplicar a transformação
imagem_corrigida = cv2.warpPerspective(imagem, matriz_perspectiva, (w, h))

# Exibir resultado
cv2.imshow('Correção de Perspectiva', imagem_corrigida)
cv2.waitKey(0)
cv2.destroyAllWindows()