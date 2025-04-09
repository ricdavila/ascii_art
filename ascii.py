import cv2
import os

# conjuntos de caracteres disponíveis
ASCII_CHARS_DEFAULT = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

ASCII_CHARS_ADVANCED = [" ", ".", "'", "`", "^", "\"", ",", ":", ";", "I", "l", "!", 
                        "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", 
                        "1", ")", "(", "|", "\\", "/", "t", "f", "j", "r", "x", "n", 
                        "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", 
                        "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", 
                        "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]            

class AsciiGenerator:
    """Classe gera o ASCII a partir de uma imagem tratada."""

    def __init__(self):
        """Inicializa o conversor de imagem para ASCII."""
        pass
        
    def gerar_ascii(self, imagem, modo):
        """
        A partir da imagem tratada, converte cada pixel da imagem para o respectivo caractere
        ASCII de acordo com o grau de luminosidade/cinza.
        """
        
        # define qual conjunto de caracteres que será utilizado
        if modo == 2:
            ascii_chars = ASCII_CHARS_ADVANCED
        else:
            ascii_chars = ASCII_CHARS_DEFAULT

        # número para representar o grau de cinza/de luminosidade
        grau_cinza = 255 / (len(ascii_chars) - 1)
        
        # armazena os caracteres ASCII
        art_ascii = ""

        # percorre cada linha e cada pixel da imagem, escolhendo um caractere ASCII correspondente
        # e adicionando-o à string principal 'art_ascii'
        for linha in imagem:
            for pixel in linha:
                indice = int(pixel/grau_cinza)
                caractere = ascii_chars[indice]
                art_ascii += caractere + " "
            art_ascii += "\n"

        # limpa o terminal
        os.system("cls")
        # escreve a string criada no terminal
        print(art_ascii)

        # salva o resultado em um arquivo de texto
        #with open("ascii_art.txt", "w") as arquivo:
        #    arquivo.write(art_ascii)

class ImageImport():
    """
    Classe que recebe o caminho da imagem e a importa, retornando uma imagem redimensionada e em
    escala de cinza.
    """

    def __init__(self):
            """Inicializa o importador de imagens."""
            pass

    def tratar_imagem(self, caminho, tamanho_maximo):
        """Função para tratar a imagem, convertendo-a para escala de cinza e redimensionando-a."""

        # importa e converte a imagem para escala de cinza
        imagem_file = cv2.imread(caminho)
        img = cv2.cvtColor(imagem_file, cv2.COLOR_BGR2GRAY)
        
        # carrega as dimensões da imagem
        largura_maxima = tamanho_maximo
        img_altura, img_largura = img.shape
        
        # verifica se a imagem possui largura maior do que a máxima suportada
        if img_largura > largura_maxima:
            # calcula a nova altura da imagem mantendo a proporção
            proporcao = img_largura / img_altura
            nova_altura = int(largura_maxima / proporcao)
            # redimensiona a imagem
            img = cv2.resize(img,(largura_maxima, nova_altura))

        return img


def start_program():
    """Primeira função a ser chamada no início do programa. Mostra o cabeçalho do programa."""

    os.system("cls")
    print("\n--------------------------------------")
    print("         IMAGEM -> ASCII")
    print("--------------------------------------")
    print("\nDigite ESC para sair.")
    print("\n- MODO: Padrão [1] ou Avançado [2]")
    print("- TAMANHO MÁXIMO: Número Inteiro (padrão = 100)")
    # abre espaço para o input de dados
    receber_dados()

def receber_dados():
    """
    Função para receber os dados do usuário referentes ao caminho da imagem, o modo
    desejado para conversão e o tamanho máximo para o resultado final.
    """
    while True:
        # recebe os dados de entrada do usuário
        dados_inseridos = input("\n\n> Insira os dados: <CAMINHO DA IMAGEM> <MODO> <TAMANHO MÁXIMO>: ").split(" ")
        
        # verifica se o usuário deseja sair do programa
        if dados_inseridos[0].upper() == "ESC":
            exit(0)
        
        # verifica a validade do caminho inserido
        # só continua o processo se o caminho for válido
        if not os.path.exists(dados_inseridos[0]):
            print("\n\n[ERRO] Caminho inválido!")
        else:
            img_path = dados_inseridos[0]
                
            # verifica se o modo inserido é válido 
            if not len(dados_inseridos) > 1:
                print("\n\n[ERRO] Insira um Modo válido para a operação.")
            elif not dados_inseridos[1].isdigit() or not int(dados_inseridos[1]) in [1, 2]:
                print("\n\n[ERRO] Modo inválido! Insira [1] para o modo PADRÃO ou [2] para o modo AVANÇADO.")
            else:
                modo = int(dados_inseridos[1])

                # verifica se um tamanho máximo foi inserido
                if len(dados_inseridos) > 2:
                    if not dados_inseridos[2].isdigit():
                        print("\n\n[ERRO] Tamanho máximo inválido! Insira um número inteiro.")                    
                    else:
                        tamanho_maximo = int(dados_inseridos[2])
                        # repassa os dados recebidos para a conversão
                        converter_imagem(img_path, modo, tamanho_maximo)       
                else:
                    converter_imagem(img_path, modo)       
            

            


def converter_imagem(img_path, modo, tamanho_maximo=100):
    """Função que recebe os dados e efetivamente converte a imagem."""

    # trata a imagem
    conversor_img = ImageImport()
    img = conversor_img.tratar_imagem(img_path, tamanho_maximo)

    # converte a imagem para ASCII
    conversor_ascii = AsciiGenerator()
    conversor_ascii.gerar_ascii(img, modo)

    # pergunta se o usuário deseja fazer mais uma conversão
    repeat = input("\n\nDeseja fazer mais uma conversão? [s/n]: ").lower() 
    
    if repeat == "s":
        os.system("cls")
        start_program()

if __name__ == "__main__":
    start_program()


        



