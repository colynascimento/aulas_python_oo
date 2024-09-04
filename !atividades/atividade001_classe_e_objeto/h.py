# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# H) Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

import os


class Tabuada:
    def __init__(self, numero):
        self.numero = numero
        
    def calcular_tabuada(self):
        lista_tabuada = list()
        
        for i in range(1, 11):
            multiplicacao = self.numero * i
            lista_tabuada.append(multiplicacao)
            
        return lista_tabuada
    
os.system('cls')

numero = int(input('Digite um número: '))
numeracao = 0

tabuada = Tabuada(numero)
lista_tabuada = tabuada.calcular_tabuada()

for multiplicacao in lista_tabuada:
    numeracao += 1
    print(f'{numero} × {numeracao} = {multiplicacao}')