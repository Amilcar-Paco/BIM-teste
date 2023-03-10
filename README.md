Para resolver o problema proposto, é necessário implementar um algoritmo que preencha uma matriz de 20x10 com as peças especificadas na sequência indicada.

A solução pode ser dividida em 3 partes principais:

### 1. Definir a estrutura das peças e seus possíveis encaixes:
Para facilitar a manipulação das peças, podemos criar uma estrutura de dados para representar cada peça. Cada peça será composta por 4 blocos, que podem ser preenchidos com um número de 1 a 6. Além disso, para cada tipo de peça, podemos definir seus possíveis encaixes, ou seja, como ela pode ser colocada em relação às peças já existentes na matriz.

### 2. Implementar a lógica de preenchimento da matriz:
O algoritmo deve percorrer a sequência de peças e tentar encaixá-las na matriz seguindo as seguintes regras:

- A base da peça deve estar encostada a outras peças em toda a sua largura, sem espaços vazios.
- A peça deve ser colocada o mais abaixo possível e da esquerda para a direita.
- Se não for possível encaixar a peça de acordo com essas regras, ela deve ser descartada e passar para a próxima peça da sequência.

### 3. Escrever o resultado no arquivo de texto:
Por fim, o resultado deve ser escrito em um arquivo de texto no formato especificado.