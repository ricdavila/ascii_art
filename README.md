# ASCII ART

Projeto pessoal desenvolvido em **Python** e com a biblioteca **OpenCV**.

## Funcionamento

Rode o script **ascii.py** e insira os dados pedidos. 

- `CAMINHO DA IMAGEM` : (str) insira o caminho *(global)* para a imagm que deseja converter.
- `MODO` : (1 ou 2) escolha entre o modo **padrão** \[1] e o modo **avançado** \[2]. O MODO de conversão se refere à quantidade de caracteres ASCII que serão utilizados para representar a imagem. Para conversões em tamanhos menores (tamanho < 200), *geralmente* obtêm-se melhores resultados com o modo **padrão**. Para tamanhos maiores, o modo **avançado** pode vir a ser útil, alcançando maior detalhamento.
- `TAMANHO DA IMAGEM` : (int) defina aqui a largura máxima da arte ASCII a ser gerada. Esse valor será utilizado como o **número máximo de caracteres por linha**. _Observação: visando melhor resultado visual, adiciona-se um espaço em branco após cada caractere, facilitando a leitura da imagem._

## Requesitos

Para o tratamento da imagem, ou seja, sua conversão em **escala de cinza** e o seu **redimensionamento**, o programa utiliza a biblioteca **OpenCV**.
Instale o pacote principal da biblioteca com o *pip*:

``
pip install opencv-python
``
Confira a [documentação](https://pypi.org/project/opencv-python/) em caso de dúvidas.
