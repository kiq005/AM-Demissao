#!/bin/python
'''
Função alvo

Atributos:
- Tempo desde contratacao [dias]
  . Quantidade de dias passados desde a contratação do funcionário
- Tempo desde promoção    [dias]
  . Quantidade de dias passados desde a última promoção do funcionário
  . Considenra-se a contratação como primeira promoção
- Faltas                  [dias]
  . Número de dias que o funcionário não foi trabalhar
- Tempo de percurso       [minutos]
  . Tempo gasto no percurso entre a casa e o trabalho
  . Para outras atividades, considera-se o tempo em transito até o local de realização desta atividade
- Carga horária           [horas]
  . Horas trabalhadas por semana
- Salário                 [Reais]
  . Salário do funcionário, sem descontos
- Renda Familiar          [Reais]
  . Renda somada de todos os moradores da casa do funcionário
- Grau de Escolaridade    [Valor]
  . Valores:
     → 0 - Analfabeto
     → 1 - Fundamental Incompleto
     → 2 - Fundamental Completo
     → 3 - Médio Incompleto
     → 4 - Médio Completo
     → 5 - Superior
     → 6 - Pós-Graduação
     → 7 - Mestrado
     → 8 - Doutorado
     → 9 - Pós-Doutorado
- Desempenho no Trabalho [Valor]
  . Valores:
     → 1 - Péssimo
     → 2 - Ruim
     → 3 - Mediano
     → 4 - Bom
     → 5 - Excepcional
- Relacionamento [Valor]
  . Relacionamento com os colegas de trabalho
  . Valores
     → 1 - Péssimo
     → 2 - Ruim
     → 3 - Mediano
     → 4 - Bom
     → 5 - Excepcional
'''

'''
Normalize
- Normaliza um valor passado
  . n - Valor a ser normalizado
  . n_min - Valor mínimo de referência
  . n_max - Valor máximo de referência
'''
def normalize(n, n_min, n_max):
  return (n-n_min)/(n_max-n_min)

# Globais
idade_empresa      = -1
salario_maximo     = -1
renda_familiar_max = -1


def func(t_cont, t_promo, faltas, trans, c_hora, salario, r_famil, escolar, desemp, relac):
  tc  = normalize(t_cont, 0, idade_empresa)
  tp = normalize(t_promo, 0, idade_empresa)
  fa  = normalize(faltas, 0, idade_empresa)
  ch  = normalize(c_hora, 0, 168)
  sl = normalize(salario, 0, salario_maximo)
  rf = normalize(r_famil, 0, renda_familiar, max)
  es = normalize(escolar, 0, 9)
  ds  = normalize(desemp, 1, 5)
  rl   = normalize(relac, 1, 5)

  return tc + tp + fa + ch + sl + rf + es + ds + rl


