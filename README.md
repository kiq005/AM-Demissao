# AM-Demissao
Uma inteligência artificial que estima a chance de um funcionário pedir demissão, construída para a disciplina de Apredizado de Máquina, na UFABC.

## Dependencias
Para rodar este programa, você irá precisar dos módulos **argparser**, **numpy** e **sklearn**, que podem ser instalados utilizando o comando **pip**:
```
pip install --user sklearn numpy argparser
```

Para visualizar as imagens será necessário **Tkinter**, que já vem instalado com a maioria das distribuições Python. Caso TKinter não esteja instalado, voce pode fazê-lo pelo seu gerenciador de pacotes:
```
# Debian/Ubuntu/Mint
apt-get install tk
# Arch based
pacman -S tk
```

## Função alvo
Para definir a função alvo, consideramos os seguintes atributos:

- Tempo desde contratacao        [anos] {2,25 - 3,2%}
  - Quantidade de dias passados desde a contratação do funcionário
- Tempo desde promoção           [anos] {3,5 - 5,0%}
  - Quantidade de dias passados desde a última promoção do funcionário
  - Considenra-se a contratação como primeira promoção
- Tempo de percurso              [minutos] {3 - 4,3%}
  - Tempo gasto no percurso entre a casa e o trabalho
  - Para outras atividades, considera-se o tempo em transito até o local de realização desta atividade
- Idade                          [Anos] {2 - 2,9%}
  - Idade do funcionário
- Número de Dependentes          [V. Numérico] {16 - 22,9%}
  - Pessoas que vivem da renda (marido/esposa, filhos, pais, ...)
- Salário                        [Reais] {8 - 11,4%}
  - Salário do funcionário, sem descontos
- Participação na Renda Familiar [Porcentagem] {24 - 34,3%}
  - Participação percentual sobre a renda somada de todos os moradores da casa do funcionário
- Grau de Escolaridade           [Valor] {1 - 1,4%}
  - Valores:
    - 0 - Analfabeto
    - 1 - Fundamental Incompleto
    - 2 - Fundamental Completo
    - 3 - Médio Incompleto
    - 4 - Médio Completo
    - 5 - Superior
    - 6 - Pós-Graduação
    - 7 - Mestrado
    - 8 - Doutorado
    - 9 - Pós-Doutorado
- Desempenho no Trabalho         [Valor] {1 - 1,4%}
  - Valores:
    - 1 - Péssimo
    - 2 - Ruim
    - 3 - Mediano
    - 4 - Bom
    - 5 - Excepcional
- Relacionamento                 [Valor] {3,75 - 5,4%}
  - Relacionamento com os colegas de trabalho
  - Valores:
    - 1 - Péssimo
    - 2 - Ruim
    - 3 - Mediano
    - 4 - Bom
    - 5 - Excepcional
- Grau de nível Hierárquico       [Grau] {5,5 - 7,9%}
  - Distância entre o funcionário e o CEO da empresa, contado por nós gerentes entre eles.
    - 0 - CEO
    - 1 - Gerente que reporta diretamente ao CEO
    - 2 - Gerente que reporta a outro gerente
    - 3 - ...

Na classificação, tres classes são consideradas:
- Irá perdir demissão nos próximos 3 meses: (1)
  - Se o valor obtido pela função considerar > 60% de chance.
- Não irá perdir demissão nos próximos 3 meses: (-1)
  - Se o valor obtido pela função considerar < 40% de chance.
- Incerto: (0)
  - Se o valor obtido pela função estiver entre 40% e 60% de chance.

## Distribuição
Para geração dos dados, as seguintes distribuições foram consideradas:

- Tempo desde contratação
  - Uniforme, entre 0 e a idade da empresa.
- Tempo desde promoção
  - Há uma chance de 33% do funcionário não ter recebido promoção, caso contrário, uniforme entre 0 e o tempo desde contratação.
- Tempo de percurso
  - Uniforme entre um tempo mínimo e máximo estabelecido (padrão: 10 e 180 minutos).
- Idade
  - Gaussiana, limitada entre 16 e 75, com valor médio `m=23+idade da empresa`, e desvio padrão `s=5+idade da empresa*1.1`.
  - A distribuição diz que:
    - Empresas novas (idade=0) possuem funcionários com aproximadamente 23 anos, variando entre 18 e 28.
    - Empresas com 2 anos possuem funcionários com aproximadamente 25 anos, variando entre 17 e 32.
    - Empresas com 10 anos possuem funcionários com aproximadamente 33 anos, variando entre 17 e 49.
    - Empresas com 20 anos possuem funcionários com aproximadamente 43 anos, variando entre 16 e 70.
- Número de Dependentes
  - Piso de uma distribuição exponencial, limitada entre 0 e 12, com `lambda=1`.
- Salário
  - Gaussiana, limitada entre um salário mínimo e máximo estabelecido (padrão: 1000 e 10000), com centralizada em 40% desse valor e com desvio padrão igual a um terço da média.
- Participação na Renda Familiar
  - Uniforme, entre 0 e 1.
- Grau de Escolaridade
  - Piso de uma distribuição gaussiana, limitada entre 0 e 9, centralizada no 5, com desvio padrão de 2.
- Desempenho no Trabalho
  - Piso de uma distribuição gaussiana, limitada entre 1 e 5, centralizada no 3.5, com desvio padrão de 1.
- Relacionamento
  - Piso de uma distribuição gaussiana, limitada entre 1 e 5, centralizada no 3.5, com desvio padrão de 1.
- Grau de nível Hierárquico
  - Toma-se o inverso do piso de uma distribuição exponencial, limitado entre 0 e o nível hierárquico máximo, com `lambda=1/nível hierárquico máximo`.

## Resultados
Três modelos de SVM foram testados, obtendo os seguintes resultados:

### SVC with linear kernel

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
|         -1.0 | 0.98      | 0.86   | 0.92     | 284     |
|          0.0 | 0.92      | 0.99   | 0.96     | 686     |
|          1.0 | 0.92      | 0.40   | 0.56     | 30      |
|    micro avg | 0.94      | 0.94   | 0.94     | 1000    |
|    macro avg | 0.94      | 0.75   | 0.81     | 1000    |
| weighted avg | 0.94      | 0.94   | 0.93     | 1000    |


### LinearSVC (linear kernel)

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
|         -1.0 | 0.97      | 0.89   | 0.93     | 284     |
|          0.0 | 0.92      | 0.99   | 0.95     | 686     |
|          1.0 | 0.50      | 0.03   | 0.06     | 30      |
|    micro avg | 0.93      | 0.93   | 0.93     | 1000    |
|    macro avg | 0.80      | 0.64   | 0.65     | 1000    |
| weighted avg | 0.92      | 0.93   | 0.92     | 1000    |


### SVC with RBF kernel

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
|         -1.0 | 0.97      | 0.88   | 0.92     | 284     |
|          0.0 | 0.93      | 0.99   | 0.96     | 686     |
|          1.0 | 0.93      | 0.43   | 0.59     | 30      |
|    micro avg | 0.94      | 0.94   | 0.94     | 1000    |
|    macro avg | 0.94      | 0.77   | 0.82     | 1000    |
| weighted avg | 0.94      | 0.94   | 0.93     | 1000    |


### SVC with polynomial (degree 3) kernel

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
|         -1.0 | 0.98      | 0.95   | 0.97     | 284     |
|          0.0 | 0.97      | 0.99   | 0.98     | 686     |
|          1.0 | 0.81      | 0.73   | 0.77     | 30      |
|    micro avg | 0.97      | 0.97   | 0.97     | 1000    |
|    macro avg | 0.92      | 0.89   | 0.91     | 1000    |
| weighted avg | 0.97      | 0.97   | 0.97     | 1000    |

### SVC with sigmoidal kernel
|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
|        -1.0  |     0.39  |   0.40 |     0.39 |      284|
|         0.0  |     0.72  |   0.70 |     0.71 |      686|
|         1.0  |     0.13  |   0.20 |     0.16 |       30|
|   micro avg  |     0.60  |   0.60 |     0.60 |     1000|
|   macro avg  |     0.41  |   0.43 |     0.42 |     1000|
|weighted avg  |     0.61  |   0.60 |     0.60 |     1000|
