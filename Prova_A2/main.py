import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from skimage import data, color
from skimage.transform import resize
import matplotlib.pyplot as plt

def preprocessar_imagem(img_rgb):
    img_resized = cv2.resize(img_rgb, (128, 128))
    img_gauss = cv2.GaussianBlur(img_resized, (5, 5), 0)
    img_cinza = cv2.cvtColor(img_gauss, cv2.COLOR_BGR2GRAY)
    img_eq = cv2.equalizeHist(img_cinza)
    return img_eq

def mostrar_imagens(imagens, titulos, rows=1, cols=2):
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))
    axes = axes.ravel() if rows > 1 or cols > 1 else [axes]
    
    for img, title, ax in zip(imagens, titulos, axes):
        if len(img.shape) == 2:
            ax.imshow(img, cmap='gray')
        else: 
            ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

def carregar_treinamento(pasta='./imagens/'):
    dados = []
    rotulos = []

    imagens_treino = [
        ('gato1.jpg', 'gato'),
        ('gato2.jpg', 'gato'),
        ('cachorro1.jpg', 'cachorro'),
        ('cachorro2.jpg', 'cachorro')
    ]

    for nome, rotulo in imagens_treino:
        caminho = os.path.join(pasta, nome)
        imagem = cv2.imread(caminho)
        if imagem is None:
            print(f"Erro ao carregar {caminho}")
            continue
        
        imagem_processada = preprocessar_imagem(imagem)
        dados.append(imagem_processada.flatten())
        rotulos.append(rotulo)

        mostrar_imagens(
            [imagem, imagem_processada],
            [f'{rotulo} - {nome} - Original', f'{rotulo} - {nome} - Processada']
        )

    return np.array(dados), np.array(rotulos)

def carregar_imagens_teste(pasta='./imagens/'):
    nomes_rotulos = [
        ('gato3.jpg', 'gato'),
        ('cachorro3.jpg', 'cachorro')
    ]
    dados = []
    rotulos = []

    for nome, rotulo in nomes_rotulos:
        caminho = os.path.join(pasta, nome)
        imagem = cv2.imread(caminho)
        if imagem is None:
            print(f"Erro ao carregar {caminho}")
            continue
        
        imagem_processada = preprocessar_imagem(imagem)
        dados.append(imagem_processada.flatten())
        rotulos.append(rotulo)

        mostrar_imagens(
            [imagem, imagem_processada],
            [f'{rotulo} - {nome} - Original', f'{rotulo} - {nome} - Processada']
        )

    return np.array(dados), np.array(rotulos)

X_train, y_train = carregar_treinamento()

modelo = KNeighborsClassifier(n_neighbors=1)
modelo.fit(X_train, y_train)

X_test, y_test = carregar_imagens_teste()

y_pred = modelo.predict(X_test)

print("📊 Relatório de Classificação:")
print(classification_report(y_test, y_pred))