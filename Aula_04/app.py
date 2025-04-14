import cv2
import numpy as np

# Lista de arquivos de imagem
arquivos = [
    r"C:\Users\perry\Documents\Facul\7 SEM\VisaoComputacional\Aula_04\rachadura3.png",
    r"C:\Users\perry\Documents\Facul\7 SEM\VisaoComputacional\Aula_04\rachadura4.png",
    r"C:\Users\perry\Documents\Facul\7 SEM\VisaoComputacional\Aula_04\rachadura5.jpeg"
]

# Processar e exibir cada imagem
for i, arquivo in enumerate(arquivos, start=3):
    image_rgb = cv2.imread(arquivo, cv2.IMREAD_COLOR)

    if image_rgb is None:
        print(f"Erro ao carregar a imagem: {arquivo}")
        continue

    imagem_cinza = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow(f"Thresholding Binário {i}", imagem_binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()
