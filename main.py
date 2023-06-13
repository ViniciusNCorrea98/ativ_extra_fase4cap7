const_A = float(input('Digite o valor da constante A: '))
const_B = float(input('Digite o valor da constante B: '))
const_C = float(input('Digite o valor da constante C: '))

import math
def equacao(const_A: float, const_B: float, const_C: float):


    if const_A == 0.0:
        if const_B != 0.0:
            print('A equação é de primeiro grau!')
            raiz = float((-1.0*const_C)/const_B)
            inclinacao = 'positiva' if const_B > 0.0 else 'negativa'
            print(f"A raíz da equação é x={raiz:.2f}")
            print(f'Além disso, a inclinação da reta é '+inclinacao)
        else:
            print(f"A equação é constante no valor de {const_C}")

    elif const_A > 0.0:
        print('A concavidade da parabola é voltada para cima!')
        vert = achar_vert(const_A,const_B,const_C)

        print(f'O ponto máximo do gráfico é em x={vert[0]:.2f} e y={vert[1]:.2f}')

        result = calcular_delta(const_A,const_B,const_C)
        print(result)
    else:
        print('A concavidade da parabola é voltada para baixo!')
        vert = achar_vert(const_A, const_B, const_C)
        print(f'O ponto mínimo do gráfico é em x={vert[0]:.2f} e y={vert[1]:.2f}')

        result = calcular_delta(const_A, const_B, const_C)
        print(result)





def calcular_delta(const_A: float, const_B: float, const_C: float) -> str:
    delta = float(const_B**2 - 4*const_A*const_C)
    print(delta)

    if delta < 0.0:
        return 'A equação não possui raíz'
    elif delta == 0.0:
        raiz = float(-const_B/2*const_A)
        return f'A raíz da parabola é em x={raiz}'
    else:
        raiz_1 = float((-const_B + math.sqrt(delta) )/ 2*const_A)
        raiz_2 = float((-const_B - math.sqrt(delta) )/ 2 * const_A)
        return f'As raízes da parabola é em x={raiz_1} e em x={raiz_2}'

def achar_vert(const_A: float, const_B: float, const_C: float) -> [float, float]:
    vert_X = float(-const_B / (2 * const_A))
    vert_Y = float(const_A * (vert_X ** 2) + const_B * vert_X + const_C)
    return vert_X, vert_Y


equacao(const_A,const_B,const_C)