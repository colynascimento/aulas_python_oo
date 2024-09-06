# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 02/09/2024
# Atividade 001 - Classe e Objeto

# A) Faça um programa que peça 3 valores, depois calcule e
# imprima  a soma e a multiplicação desses valores. 

import os
import time


class Operacoes:
    def __init__(self, valor_1, valor_2, valor_3):
        self.valor_1 = valor_1
        self.valor_2 = valor_2
        self.valor_3 = valor_3
        
    def soma(self):
        return self.valor_1 + self.valor_2 + self.valor_3
    
    def multiplicacao(self):
        return self.valor_1 * self.valor_2 * self.valor_3
    
    def validar_numero(self):
        try:
            self.valor_1 = int(self.valor_1) 
            self.valor_2 = int(self.valor_2) 
            self.valor_3 = int(self.valor_3)
            return True
        except ValueError:
            return False
    
os.system('cls')

while True:
    print('_' * 60)
    print('\nSeja bem-vindo ao programa!')
    print('Vamos fazer operações matemáticas.')
    print('_' * 60)

    valor_1 = input('\nDigite o primeiro valor: ')
    valor_2 = input('Digite o segundo valor: ')
    valor_3 = input('Digite o terceiro valor: ')

    resultado = Operacoes(valor_1, valor_2, valor_3)

    if not resultado.validar_numero():
        
        os.system('cls')
        
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
        continue


    os.system('cls')

    while True:
        print(' Operações Matemáticas')
        print('\n     1 - Soma')
        print('     2 - Multiplicação')
        print('_' * 60)

        opcao = input('     Digite a operação escolhida (1 ou 2): ')


        if opcao == '1':
            print(f'Somando {valor_1} + {valor_2} + {valor_3}...')
            time.sleep(1)
            print(f'O resultado da operação é {resultado.soma()}')
            break
        elif opcao == '2':
            print(f'Multiplicando {valor_1} × {valor_2} × {valor_3}...')
            time.sleep(1)
            print(f'O resultado da operação é {resultado.multiplicacao()}')
            break
        else:
            os.system('cls')
            print('Digite uma opção válida!')
            print('_' * 60)
            print()
    break

print('_' * 70)
print('\nFim do programa')
print()
