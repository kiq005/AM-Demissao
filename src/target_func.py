#!/bin/python
import math
import random
import argparse
import numpy as np

'''
Math functions
'''
def normalize(n, n_min, n_max):
  return (n-n_min)/(n_max-n_min)

def lin(x, xi, yi, xf, yf):
    dy = yf-yi
    dx = (x-xi)/(xf-xi)
    return dy*dx+yi

def par(x, xi, yi, xf, yf):
    dy = yf-yi
    dx = (x-xi)/(xf-xi)
    return -dy*dx*dx+2*dy*dx+yi

def sig(x, xi, yi, xf, yf, k):
    dy = yf-yi
    xm = (xi+xf)/2
    return (dy/(1+math.e**(-k*(x-xm))))+yi

def gau(x, xi, yi, xf, yf, k):
    dy = yf-yi
    xm = (xi+xf)/2
    return dy*math.e**(-k*(x-xm)**2)+yi

def gauss_rand(nmin, nmax, mu, sigma):
    return min(nmax, max(nmin, random.gauss(mu, sigma)))

def exp_rand(nmin, nmax, lambd):
    return min(nmax, max(nmin, random.expovariate(lambd)))

'''
Atributes
'''
def tempo_percurso(x_tp, tempo_percurso_max):
    return lin(x_tp, 0, 0.1, tempo_percurso_max, 0.9)

def salario(x_sal, salario_max):
    return par(x_sal, 0, 0.9, salario_max, 0.1)

def part_renda_familiar(x_rend):
    return lin(x_rend, 0, 0.65, 1, 0.1)

def relacionamento(x_rel):
    return lin(x_rel, 1, 0.9, 5, 0.1)

def grau_hierarquico(x_gra, grau_hierarquico_max):
    return lin(x_gra, 0, 0.05, grau_hierarquico_max, 0.5)

def desempenho(x_des):
    return sig(x_des, 0,0.3,5,0.1,2)+gau(x_des, 1, 0.0,3, .2, 5)

def tempo_ultima_promocao(x_up):
    return sig(x_up, 0, .1, 10, .9, 2)

def idade(x_id):
    return sig(x_id, 15, .1, 31, 1.5,.6) * sig(x_id, 15, 1.5,27,.1,.1)

def grau_escolaridade(x_esc):
    return sig(x_esc, 4, .3, 5, .8, 5) * sig(x_esc, 6, 1, 7, .1, 2)

def tempo_contratacao(x_cont):
    return (sig(x_cont, 0, .3, 1, .7, 10) + sig(x_cont, 0, .6, .5, 0, 20)) * sig(x_cont, 0, 1, 4, 0.1, 2)

def num_dependentes(x_dep, x_rend):
    return -.4 * x_dep -.4 * x_rend * x_dep + .9

'''
Target Function
'''
def func(t_cont, t_promo, t_perc, i_func, n_dep, sal, p_renda, escolar, desemp, relac, hier, tp_max, sal_max, h_max):
    tc = tempo_contratacao(t_cont)
    tu = tempo_ultima_promocao(t_promo)
    tp = tempo_percurso(t_perc, tp_max)
    ida= idade(i_func)
    nd = num_dependentes(n_dep, p_renda)
    sa = salario(sal, sal_max)
    pr = part_renda_familiar(p_renda)
    ge = grau_escolaridade(escolar)
    de = desempenho(desemp)
    re = relacionamento(relac)
    hi = grau_hierarquico(hier, h_max)
    return .032*tc + .050*tu + .043*tp + .029*ida + .229 * nd + .114 * sa + .343 * pr + .014 * ge + .014 * de + .054 * re + .079*hi

'''
Data generation
'''
def gen(n, idade_empresa, tp_min, tp_max, salario_min, salario_max, hier_max, dep_max):
    db = []
    for i in range(0, n):
        tc = random.uniform(0, idade_empresa) 
        tu = tc if (random.random() < .333) else random.uniform(0, tc)
        tp = random.uniform(tp_min, tp_max)
        ida= gauss_rand(16, 75, 23+idade_empresa, 5+idade_empresa*1.1)
        nd = math.floor(exp_rand(0, 12, 1))
        sa = gauss_rand(salario_min, salario_max, (salario_min+salario_max)*.4, (salario_min+salario_max)/6)
        pr = random.random()
        es = math.floor(gauss_rand(0, 9, 5, 2))
        de = math.floor(gauss_rand(1, 5, 3.5, 1))
        re = math.floor(gauss_rand(1, 5, 3.5, 1)) 
        hi = hier_max - math.floor(exp_rand(0, hier_max, (hier_max-2)/(hier_max)))

        out = func(tc, tu, tp, ida, nd, sa, pr, es, de, re, hi, tp_max, salario_max, hier_max)

        if out > .6:
            out = 1
        elif out < .4:
            out = -1
        else:
            out = 0 
        db.append([normalize(tc, 0, idade_empresa),
                   normalize(tu, 0, idade_empresa),
                   normalize(tp, tp_min, tp_max),
                   normalize(ida, 15, 100),
                   normalize(nd,0,dep_max),
                   normalize(sa, salario_min, salario_max),
                   pr,
                   normalize(es, 0, 9),
                   normalize(de, 1, 5),
                   normalize(re, 1, 5),
                   normalize(hi, 0, hier_max),
                   out])
    return db

'''
Arguments
'''
parser = argparse.ArgumentParser(description="Generate data for training")
parser.add_argument('file', metavar='file', type=str, help='File to export the generated data')
parser.add_argument('--seed', metavar='seed', type=int, help='Seed for the random number generator', default=10)
parser.add_argument('--n', metavar='num', type=int, help='Number of samples to generate', default=10000)
parser.add_argument('--i', metavar='age', type=int, help='The age of the company', default=8)
parser.add_argument('--tmin', metavar='tmin', type=int, help='Minimum travelling time to the workplace', default=10)
parser.add_argument('--tmax', metavar='tmax', type=int, help='Maximum travelling time to the workplace', default=180)
parser.add_argument('--smin', metavar='smin', type=int, help='Minimum salary', default=1000)
parser.add_argument('--smax', metavar='smax', type=int, help='Maximum salary', default=10000)
parser.add_argument('--hmax', metavar='hmax', type=int, help='Number of hierarchical levels', default=8)
parser.add_argument('--dmax', metavar='dmax', type=int, help='Maximum number of dependents', default=12)

'''
Main Function
'''
def main():
    args = parser.parse_args()
    random.seed(args.seed)
    n = args.n
    idade_empresa = args.i
    tp_min = args.tmin
    tp_max = args.tmax
    salario_min = args.smin
    salario_max = args.smax
    hier_max = 8 
    dep_max = 12
    db = gen(n, idade_empresa, tp_min, tp_max, salario_min, salario_max, hier_max, dep_max)
    
    np.save(args.file, db)

if __name__ == '__main__':
    main()

