import math
from sympy import symbols, diff, cos
import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify

def poli_taylor(funcao, ordem, ponto):
    
    x = symbols('x')
    f = funcao(x)
    f0 = f.subs(x, ponto)
    polinomio = f0
    
    for i in range(1, ordem + 1):
        derivada = diff(f, x, i)
        derivada_ponto = derivada.subs(x, ponto)
        termo = (derivada_ponto / math.factorial(i)) * (x - ponto)**i
        polinomio += termo
        
    return polinomio



def plot_funcao_e_taylor(funcao, ponto, ordens, intervalo):
    x = symbols('x')
    f_expr = funcao(x)
    f_lamb = lambdify(x, f_expr, 'numpy')
    
    x_vals = np.linspace(*intervalo, 500)
    plt.figure(figsize=(10,6))
    plt.plot(x_vals, f_lamb(x_vals), label='Função original', linewidth=2, color='black')

    for ordem in ordens:
        pn = poli_taylor(funcao, ordem, ponto)
        pn_lamb = lambdify(x, pn, 'numpy')
        plt.plot(x_vals, pn_lamb(x_vals), label=f'P{ordem}(x)', linestyle='--')

    plt.title("Aproximação por Polinômios de Taylor")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_erros(funcao, ponto, ordens, intervalo, tipo='absoluto'):
    """
    tipo: 'absoluto' ou 'relativo'
    """
    x = symbols('x')
    f_expr = funcao(x)
    f_lamb = lambdify(x, f_expr, 'numpy')
    x_vals = np.linspace(*intervalo, 500)
    f_vals = f_lamb(x_vals)

    plt.figure(figsize=(10,6))

    for ordem in ordens:
        pn = poli_taylor(funcao, ordem, ponto)
        pn_lamb = lambdify(x, pn, 'numpy')
        pn_vals = pn_lamb(x_vals)
        
        if tipo == 'absoluto':
            erro = np.abs(f_vals - pn_vals)
            ylabel = "Erro absoluto"
        else:
            erro = np.abs(f_vals - pn_vals) / np.abs(f_vals)
            erro[f_vals == 0] = 0  # evitar divisão por zero
            ylabel = "Erro relativo"

        plt.plot(x_vals, erro, label=f'Ordem {ordem}')

    plt.title(f"{ylabel} da aproximação de Taylor")
    plt.xlabel("x")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    funcao = cos
    ponto = 0
    ordens = [1, 2, 3, 4, 5]
    intervalo = (-5,5)
    
    plot_funcao_e_taylor(funcao, ponto, ordens, intervalo)
    plot_erros(funcao, ponto, ordens, intervalo, tipo='absoluto')
    
    
