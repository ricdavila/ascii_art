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

        art_ascii = "\n\n\n                                     "

        for linha in imagem:
            for pixel in linha:
                indice = int(pixel/grau_cinza)
                caractere = ascii_chars[indice]
                art_ascii += caractere + " "
            art_ascii += "\n                                    "

        os.system("cls")
        print(art_ascii)

        # salva o resultado em um arquivo de texto
        with open("ascii_art.txt", "w") as arquivo:
            arquivo.write(art_ascii)



    

def start_program():
    print("\n--------------------------------------")
    print("        CONVERSOR IMAGEM -> ASCII")
    print("--------------------------------------")
    print("\nDigite ESC para sair.")
    print("\nINSIRA: <CAMINHO DA IMAGEM> <MODO> <TAMANHO MÁXIMO>")
    print("\nMODO: PADRÃO [1] ou AVANÇADO [2]")
    print("TAMANHO MÁXIMO: int (padrão = 100)")

    dados_inseridos = input("\nDigite os dados: ").split(" ")
    if dados_inseridos[0] == "ESC":
        exit(0)
    elif len(dados_inseridos) == 3:
        img_path = dados_inseridos[0]
        modo = int(dados_inseridos[1])
        tamanho_maximo = int(dados_inseridos[2])

    AsciiGenerator(img_path, modo, tamanho_maximo)

    repeat = input("\n\nDeseja fazer mais uma conversão? [s/n]: ").lower() 
    
    if repeat == "s":
        os.system("cls")
        start_program()


if __name__ == "__main__":
    start_program()


        



