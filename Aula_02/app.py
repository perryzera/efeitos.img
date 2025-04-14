import cv2

# Verificamos o Shape da Imagem
# Consiste na representação de uma tupla que define o tam da imagem

name_of_img_file = r"C:\Users\perry\Documents\Facul\7 SEM\VisaoComputacional\Aula_02\praia.jpg"

def img_rgb(name_of_img_file):
    return cv2.imread(
        name_of_img_file,
        cv2.IMREAD_COLOR
    )

def shape_of_image(name_of_img_file, image_rgb):
    print ("Exibe o shape da imagem")

    image_cinza = cv2.imread(
        name_of_img_file,
        cv2.IMREAD_GRAYSCALE
    )

    print ("Dimensão da imagem em escala cinza:", image_cinza.shape)
    print ("Dimensão da imagem em escala cinza:", image_rgb.shape)


def gausssian_blur(image_rgb): 
    # GaussianBlur(
    # src -> objeto que representa a imagem
    # ksize -> tamanho do kernel de connvolução (width, height)
    # deve sempre em valor impar, ksize aumenta o desfoque, quanto
    # maior for o seu valor, mais a imagem ficará desfocada
    # sigmaX -> Desvio padrao Gaussiano no eixo X
    # sigaY -> Desvio padrão no eixo Y
    # Para não complicar o entendimento do filtro, neste momento
    # vamos lidar com o sigmaX sempre como 0 (o y como
    # não passado, receve um default de 0 também)

    KSIZE = (3,3)
    SIGMA_X = 0
    TITLE_OF_IMAGE_RGB = "Original"
    TITLE_OF_IMAGE_BLUR = "Blur"

    image_blur = cv2.GaussianBlur(
                    image_rgb,
                    KSIZE,
                    SIGMA_X
                )

    # Apresenta: Imagem RGB
    cv2.imshow(TITLE_OF_IMAGE_RGB, image_rgb)
    # Apresenta: Imagem com Filtro Aplicado    
    cv2.imshow(TITLE_OF_IMAGE_BLUR, image_blur)

    # Aguarda a tecla 0 ser pressionado para continuar o código
    # a intenção é permitir que o usuário visualize a imagem
    # caso contrario ela aparece rapidamente, e é fechada
    cv2.waitKey(0)

    # Destrói todas as janelas
    cv2.destroyAllWindows

# Invocando a Função que Cria o Objeto RGB
image_rgb = img_rgb(name_of_img_file)

# Chamando a Função que Exibe o Shape
shape_of_image(name_of_img_file, image_rgb)

# Aplicando o Filtro Blur
gausssian_blur(image_rgb)