from politaylor import poli_taylor
from scipy.integrate import quad
from sympy import exp, Symbol, diff, lambdify, integrate

'''
escrita:
apresetnar  o polinomio de taylor da funcao f escolhida para cada ordem n
determinar o intervalo da integracao
apresentar a integral do poli de taylor para cada ordem n
fazer tabela comparando cada integral de ordem n com o valor obtido pela funcao scipy.integrate.quad

dev:
objetivo: integrar a funcao f escolhida
- gerar o polinomio de taylor de ordens 3, 5 e 7
- apresentar o polinomio
criar funcao pra integrar
- funcao pra calcular a primitiva
- calcular a primitiva de cada termo e somar no loop
calcular a integral para cada ordem n
'''

def my_func(x):
    return

def primitiva_termo(termo, variavel):
    return integrate(termo, variavel)

def integral_poli_taylor(funcao, ordem, intervalo_integracao):
    
    myPolyTaylor = poli_taylor(funcao, ordem, 0)
    #print(myPolyTaylor)
    extremo1, extremo2 = intervalo_integracao

    integral = 0
    termos = myPolyTaylor.as_ordered_terms() #retorna lista com cada termo
    x = Symbol('x')
    for termo in termos:
        '''
        gerar a primiriva para cada termo
        calcular numericamente a primitiva para os extremos
        calcular diferenca
        incrementar o valor a 'integral'
        '''

        primitiva = primitiva_termo(termo, x)
        #print(primitiva)
        prim_extremo1 = primitiva.subs(x, extremo1)
        #print(prim_extremo1)
        prim_extremo2 = primitiva.subs(x, extremo2)
        #print(prim_extremo2)
        integral_termo = abs(prim_extremo1-prim_extremo2)

        integral += integral_termo
    return integral

def main():
    x = Symbol('x')
    f = lambda x: exp(-x**2) #pra usar ela na funcao de derivacao, diff, tem q usar f(x) !!!
    ordens = [3,5,7, 10]
    intervaloIntegracao = (-4, 4)
    valores_integral = []

    for ordem in ordens:
        integral_no_intervalo = integral_poli_taylor(f, ordem, intervaloIntegracao)
        valores_integral.append(integral_no_intervalo)

    print(valores_integral)
        


if __name__=='__main__':
    main()

    