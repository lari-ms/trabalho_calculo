from poli_taylor import poli_taylor
from scipy.integrate import quad
from sympy import exp, Symbol, integrate, pretty, lambdify

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

def primitiva_termo(termo, variavel):
    return integrate(termo, variavel)

def integral_poli_taylor(funcao, ordem, intervalo_integracao, ponto_expans=0):
    
    myPolyTaylor = poli_taylor(funcao, ordem, ponto_expans)
    #print(f'polinomio de ordem n={ordem} {pretty(myPolyTaylor)}')
    extremo1, extremo2 = intervalo_integracao

    integral = 0
    termos = myPolyTaylor.as_ordered_terms() #retorna lista com cada termo
    #print(termos)
    x = Symbol('x')
    for termo in termos:
        '''
        gerar a primiriva para cada termo
        calcular numericamente a primitiva para os extremos
        calcular diferenca
        incrementar o valor a 'integral'
        '''
        #print(f'termo: {termo}')
        primitiva = primitiva_termo(termo, x)
        #print(f'primitiva: {primitiva}')
        prim_extremo1 = float((primitiva.subs(x, extremo1)).evalf())
        #print(f'prim extremo 1: {prim_extremo1}')
        prim_extremo2 = float((primitiva.subs(x, extremo2)).evalf())
        #print(f'prim extremo2: {prim_extremo2}')
        integral_termo = prim_extremo2-prim_extremo1
        #print(f'ext2-ext1: {integral_termo}')
        #print()

        integral += integral_termo
    
    #integral = float(abs(integral).evalf())
    #print(f'integral no intervalo {intervalo_integracao} =     {integral}')

    return integral

def main():
    x = Symbol('x')
    f = lambda x: exp(-x**2) #pra usar ela na funcao de derivacao, diff, tem q usar f(x) !!!
    ordens = [3, 5, 7]
    intervaloIntegracao = (-2, 2)
    valores_integral = []

    for ordem in ordens:
        integral_no_intervalo = integral_poli_taylor(f, ordem, intervaloIntegracao)
        valores_integral.append(integral_no_intervalo)

    print(f'valores obtidos para cada ordem: {valores_integral}')

    val_referencia, _= quad(lambdify(x, exp(-x**2), 'numpy'),intervaloIntegracao[0], intervaloIntegracao[1])
    print(f'valor de referencia: {val_referencia}')
    vals_erro = [abs(valor-val_referencia) for valor in valores_integral]
    print(f'valores de erro (funcao implementada - scipy.integrate.quad): {vals_erro}')
        


if __name__=='__main__':
    main()

    