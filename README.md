# ASCII ART

Projeto pessoal desenvolvido em **Python** e com a biblioteca **OpenCV** para converter imagens em Arte ASCII. Para esse processamento, o programa importa a imagem solicitada, converte-a para escala de cinza, redimensiona-a e então converte cada pixel em um caractere ASCII. 


![borboleta monarca](https://github.com/ricdavila/ascii_art/blob/25449f7bc0b72c19568ca211d726cb0c3a6b93d9/imgs/monarch_eg.png)


## Instalação

1. Clone o repositório:
```
git clone https://github.com/ricdavila/ascii_art.git
   
cd ascii_art
```

2. Instale as dependências (biblioteca *OpenCV*):
```
pip install opencv-python
```


## Como Usar

Execute o script **ascii.py**:

    python ascii.py

Quando solicitado, insira os dados para a conversão. Por exemplo:

    Insira os dados: caminho\da\sua\imagem.png 1 120

Para sair do programa digite `ESC`.

### Parâmetros do Programa

- `CAMINHO DA IMAGEM` : (str) insira o caminho *(global)* para a imagem que deseja converter.

- `MODO` : (1 ou 2) escolha entre o modo **padrão** \[1] e o modo **avançado** \[2]. O MODO de conversão se refere à quantidade de caracteres ASCII que serão utilizados para representar a imagem. Para conversões em tamanhos menores (tamanho < 200), *geralmente* geram-se melhores resultados com o modo **padrão**. Para tamanhos maiores, o modo **avançado** pode vir a ser útil, alcançando maior detalhamento.

Para o modo **padrão**, utilizam-se 12 caracteres :

    " ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"

Para o modo **avançado**, utilizam-se 70 caracteres :
 
    " ", ".", "'", "`", "^", "\"", ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "\\", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"

- `TAMANHO DA IMAGEM` : (int) defina aqui a largura máxima da arte ASCII a ser gerada. Esse valor será utilizado como o **número máximo de caracteres por linha**.

## Funcionamento

O script segue este fluxo de processamento : 

#### 1. Input de Dados
- Leitura de dados inseridos pelo usuário;
- As informações são validadas e então repassadas para a classe de tratamento das imagens.

#### 2. Processasmento da Imagem
- A imagem é importada e carregada;
- Conversão para escala de cinza;
- Redimensionamento da imagem, caso necessário, mantendo a proporção original.

#### 3. Mapeamento ASCII
- Cada pixel da imagem é convertido para um caractere ASCII;
- A conversão pauta-se na intensidade luminosa do pixel — caracteres mais 'densos', como '#' e '@', são utilizados para representar pixels mais claros.
- Já para pixels menos luminosos, utiliza-se caracteres menos densos, como ',' ou ' '.
- Para melhor visualização, um espaço em branco é adicionado após cada caractere.

#### 4. Exibição
- A arte ASCII final é exibida no terminal.

## Exemplos

![castelo](https://github.com/ricdavila/ascii_art/blob/8303456b0e482e71deeab5fe9004e8c68f1f37da/imgs/ascii_castle.png)

![gato](https://github.com/ricdavila/ascii_art/blob/cb3a7b32dd46f9644e392e47b5ada05b1cb4d85c/imgs/ascii_cat.png)

## Possíveis Melhorias
- Suporte para caracteres coloridos;
- Permitir customização dos caracteres a serem utilizados;
- Suporte para manipulação da imagem importada (inversão de cores, modificação do contraste, etc.);
- Adicionar interface visual;

---

Desenvolvido com muito 🤍 e ☕ utilizando Python 🐍. Deseja conferir outros projetos? Acesse [meu perfil](https://github.com/ricdavila).

