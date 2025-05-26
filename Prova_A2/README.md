# Classificador de Imagens #
    Esse projeto consiste no pipeline de prática de técnicas de Visão Computacional e Machine Learning para carregar, pré-processar, e por mim, classificar os modelos testados.

# Estrutura do Teste
    Prova_A2/
    ├── imagens/
    │   ├── gato1.jpg
    │   ├── gato2.jpg
    │   ├── gato3.jpg
    │   ├── cachorro1.jpg
    │   ├── cachorro2.jpg
    │   └── cachorro3.jpg  
    ├── main.py
    ├── requirements.txt
    └── README.me

# Tecnologias Utilizadas
    Python3 (linguagem do projeto)
    OpenCV2 (Redimensionamento 128x128, filtro Gaussiano e Equalização do Histograma)
    NumPy (Manipula os Arrays e transforma as imagens em Vetores numéricos)
    Scikit-learn (Separa os dados em treino teste, Classificação KNN e gera as métricas de avaliação)
    Scikit-image (Recebe imagens para o treinamento)
    Matplotlib (Exibe as imagens)

# Metodologia
> Pré-processamento
    - Redimensionamento das imagens para o padrão de 128x128
    - Aplicação do filtro Guassiano
    - Conversão para cinza
    - Equalização do Histograma

> Treinamento
    - O modelo é treinado com as imagens do 'sick-image'

> Classificação
    - Por fim, as imagens são carregadas da pasta './imagens/' 
    - O modelo resulta se a imagem é classificada como 'gato' ou 'cachorro' para cada uma das imagens testadas
    - É exibido as métricas de avaliação (precisão, recall e F1-score)

# Como Executar o Teste
    1. Baixe a pasta 'Prova_A2'
    2. Abra o Terminal (CTRL + SHIFT + ')
    3. Execute:
        3.1 pip install requirements.txt
        3.2 python main.py
