import cv2
import os


class AsciiGenerator:
    def __init__(self):
        
        #img_tratada = self.tratar_imagem(R"ASCII_ART\monarch.jpg")
        img_tratada = self.tratar_imagem(R"C:\Users\Usuario\Desktop\Arquivos\CODE\ASCII_ART\monarch.jpg")
        self.gerar_ascii(img_tratada)

    def gerar_ascii(self, imagem):
        
        # caracteres para a representação em ASCII
        #ascii_chars =["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", "."]
        #ascii_chars = [" ", ".", "'", "`", "^", "\"", ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "\\", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]
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


    def tratar_imagem(self, imagem):
        """
        Função para tratar a imagem, convertendo-a para escala de cinza e redimensionando-a.
        """
        # converte a imagem para escala de cinza
        image = cv2.imread(imagem)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        
        # carrega as dimensões da imagem
        largura_maxima = 100
        img_altura, img_largura = img.shape
        
        # verifica se a imagem possui largura maior do que a máxima suportada
        if img_largura > largura_maxima:
            # calcula a nova altura da imagem mantendo a proporção
            proporcao = img_largura / img_altura
            nova_altura = int(largura_maxima / proporcao)

            print(nova_altura, largura_maxima)
            # redimensiona a imagem
            img = cv2.resize(img,(largura_maxima, nova_altura))

        return img
    

    

        

if __name__ == "__main__":
    AsciiGenerator()




