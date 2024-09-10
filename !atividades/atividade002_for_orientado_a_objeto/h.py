# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# h) Faça um programa que imprima os valores no intervalo
# definidos pelo usuário.  Defina 3 números que deverão ser
# ignorados, ou seja, que não serão impressos na tela.

import os


class Contador:
    def __init__(self, valor_inicial, valor_limite, numero_ignorado1, numero_ignorado2, numero_ignorado3):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
        self.numero_ignorado1 = numero_ignorado1
        self.numero_ignorado2 = numero_ignorado2
        self.numero_ignorado3 = numero_ignorado3

    def pular_numeros(self, valor_inicial, valor_limite, numero_ignorado1, numero_ignorado2, numero_ignorado3):
        pass

class PularNumeros(Contador):
    def __init__(self, valor_inicial, valor_limite, numero_ignorado1, numero_ignorado2, numero_ignorado3):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
        self.numero_ignorado1 = numero_ignorado1
        self.numero_ignorado2 = numero_ignorado2
        self.numero_ignorado3 = numero_ignorado3

    def pular_numeros(self):
        for numero in range(self.valor_inicial, self.valor_limite + 1):
            if (numero == self.numero_ignorado1) or (numero == self.numero_ignorado2) or (numero == self.numero_ignorado3):
                continue
            print(numero, end='\n')

os.system('cls')

valor_inicial = int(input('Digite o número inicial do intervalo: '))
valor_final = int(input('Digite o número final do intervalo: '))

contador = PularNumeros(valor_inicial, valor_final, 1, 13, 27)

contador.pular_numeros()