# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# D) Faça um programa que imprima os números pares entre 0
# e 100.

import os


class Contador:
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
    
    def printar(self):
        pass

class PrintarNumero(Contador):
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite

    def printar(self):
        for i in range(self.valor_inicial, self.valor_limite):
            if i % 2 == 0:
                print(f'{i}', end=' ')

os.system('cls')

contador = PrintarNumero(0, 101)

contador.printar()