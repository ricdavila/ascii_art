import cv2
import os

class AsciiGenerator:
    def __init__(self, path, modo=1, tamanho_maximo=100):

        # trata a imagem recebida
        img_tratada = self.tratar_imagem(path, tamanho_maximo)
        # gera a string com a conversão para ASCII
        self.gerar_ascii(img_tratada, modo)
        
    def tratar_imagem(self, imagem, tamanho_maximo):
        """
        Função para tratar a imagem, convertendo-a para escala de cinza e redimensionando-a.
        """
        # converte a imagem para escala de cinza
        image = cv2.imread(imagem)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
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
    def gerar_ascii(self, imagem, modo):
        
        # caracteres para a representação em ASCII
        if modo == 2:
            ascii_chars = [" ", ".", "'", "`", "^", "\"", ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "\\", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]            
        else:
            ascii_chars = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

        # número para representar o grau de cinza/de luminosidade
        grau_cinza = 255 / (len(ascii_chars) - 1)

        art_ascii = ""

        for linha in imagem:
            for pixel in linha:
                indice = int(pixel/grau_cinza)
                caractere = ascii_chars[indice]
                art_ascii += caractere + " "
            art_ascii += "\n"

        os.system("cls")
        print(art_ascii)

        # salva o resultado em um arquivo de texto
        with open("ascii_art.txt", "w") as arquivo:
            arquivo.write(art_ascii)



    

def start_program():
    # cabeçalho do programa
    os.system("cls")
    print("\n--------------------------------------")
    print("         IMAGEM -> ASCII")
    print("--------------------------------------")
    print("\nDigite ESC para sair.")
    print("\n- MODO: Padrão [1] ou Avançado [2]")
    print("- TAMANHO MÁXIMO: Número Inteiro (padrão = 100)")

    receber_dados()


def receber_dados():

    # recebe os dados de entrada do usuário
    dados_inseridos = input("\n\n> Insira os dados: <CAMINHO DA IMAGEM> <MODO> <TAMANHO MÁXIMO>: ").split(" ")
    
    # verifica se o usuário deseja sair do programa
    if dados_inseridos[0].upper() == "ESC":
        exit(0)
    
    # verifica a validade do caminho inserido
    if os.path.exists(dados_inseridos[0]):
        img_path = dados_inseridos[0]
    else:
        print("\n\n[ERRO] Caminho inválido!")
        receber_dados()
    
    # verifica se o modo inserido é válido 
    if int(dados_inseridos[1]) == 1 or int(dados_inseridos[1]) == 2:
        modo = int(dados_inseridos[1])
    else:
        print("\n\n[ERRO] Modo inválido! Insira [1] para o modo PADRÃO ou [2] para o modo AVANÇADO.")
        receber_dados()
    
    # verifica se um tamanho máximo foi inserido
    if len(dados_inseridos) == 3:
        if dados_inseridos[2].isdigit():
            tamanho_maximo = int(dados_inseridos[2])
        else:
            print("\n\n[ERRO] Tamanho máximo inválido! Insira um número inteiro.")
            receber_dados()
    else:
        tamanho_maximo = 100
 
    # gera e exibe o ASCII a partir dos dados inseridos
    AsciiGenerator(img_path, modo, tamanho_maximo)

    # pergunta se o usuário deseja fazer mais uma conversão
    repeat = input("\n\nDeseja fazer mais uma conversão? [s/n]: ").lower() 
    
    if repeat == "s":
        os.system("cls")
        start_program()


if __name__ == "__main__":
    start_program()


        



