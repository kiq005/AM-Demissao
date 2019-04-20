# AM-Demissao
Uma inteligência artificial que estima a chance de um funcionário pedir demissão, construída para a disciplina de Apredizado de Máquina, na UFABC.

## Função alvo
Para definir a função alvo, consideramos os seguintes atributos:

- Tempo desde contratacao [dias]
  - Quantidade de dias passados desde a contratação do funcionário
- Tempo desde promoção    [dias]
  - Quantidade de dias passados desde a última promoção do funcionário
  - Considenra-se a contratação como primeira promoção
- Tempo de percurso       [minutos]
  - Tempo gasto no percurso entre a casa e o trabalho
  - Para outras atividades, considera-se o tempo em transito até o local de realização desta atividade
- Idade                   [Anos]
  - Idade do funcionário
- Número de Dependentes   [V. Numérico]
  - Pessoas que vivem da renda (marido/esposa, filhos, pais, ...)
- Salário                 [Reais]
  - Salário do funcionário, sem descontos
- Renda Familiar          [Reais]
  - Renda somada de todos os moradores da casa do funcionário
- Grau de Escolaridade    [Valor]
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
- Desempenho no Trabalho [Valor]
  - Valores:
    - 1 - Péssimo
    - 2 - Ruim
    - 3 - Mediano
    - 4 - Bom
    - 5 - Excepcional
- Relacionamento [Valor]
  - Relacionamento com os colegas de trabalho
  - Valores:
    - 1 - Péssimo
    - 2 - Ruim
    - 3 - Mediano
    - 4 - Bom
    - 5 - Excepcional
- Grau de nível Hierárquico [Grau]
  - Distância entre o funcionário e o CEO da empresa, contado por nós gerentes entre eles.
    - 0 - CEO
    - 1 - Gerente que reporta diretamente ao CEO
    - 2 - Gerente que reporta a outro gerente
    - 3 - ...
