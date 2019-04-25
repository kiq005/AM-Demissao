# AM-Demissao
Uma inteligência artificial que estima a chance de um funcionário pedir demissão, construída para a disciplina de Apredizado de Máquina, na UFABC.

## Função alvo
Para definir a função alvo, consideramos os seguintes atributos:

- Tempo desde contratacao        [dias] {2,25 - 3,2%}
  - Quantidade de dias passados desde a contratação do funcionário
- Tempo desde promoção           [dias] {3,5 - 5,0%}
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
