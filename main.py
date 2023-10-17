#Boas práticas de programação
import math
import this
this.opcao = -1

def somar(num1, num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Impossível dividir por zero!'

def tabuada(num1):
    for i in range(1,11,1):
        print('{} * {} = {}'.format(i,num1, i*num1))

def potencia(base,expoente):
    return math.pow(base,expoente)

def raiz(num):
    return math.sqrt(num)

def menu():
    print('Escolha uma das opções abaixo: \n\n'
        + '0. Sair\n'
        + '1. Soma\n'
        + '2. Subtração\n'
        + '3. Multiplicação\n'
        + '4. Divisão\n'
        + '5. Tabuada\n'
        + '6. Potência\n'
        + '7. Raiz\n')
    this.opcao = int(input())

def operacao(opcao):
    if opcao != 0:
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe um segundo número: '))

        if (opcao == 1):
            print('A soma de {} e {} é {}'.format(num1, num2, somar(num1, num2)))
        elif (opcao == 2):
            print('A subtração de {} e {} é {}'.format(num1, num2, subtrair(num1, num2)))
        elif (opcao == 3):
            print('A multiplicação de {} e {} é {}'.format(num1, num2, multiplicar(num1, num2)))
        elif (opcao == 4):
            print('A divisão de {} e {} é {}'.format(num1, num2, dividir(num1, num2)))
        elif (opcao == 5):
            print('A tabuada de de {} é: '.format(num1))
            tabuada(num1)

            print('\nA tabuada de {} é: '.format(num2))
            tabuada(num2)
        elif (opcao == 6):
            print('A potência de {} elevado a {} é: {}'.format(num1, num2, potencia(num1, num2)))
            print('\nA potência de {} elevado a {} é: {}'.format(num2, num1, potencia(num2, num1)))
        elif (opcao == 7):
            print('\nA raiz de {} é: {}'.format(num1, raiz(num1)))
            print('\nA raiz de {} é: {}'.format(num2, raiz(num2)))
    else:
        print('Obrigado!')

def chamarMenuOperacao():
    while (this.opcao != 0):
        menu()
        operacao(this.opcao)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chamarMenuOperacao()#Chamando a execução de apenas um método



