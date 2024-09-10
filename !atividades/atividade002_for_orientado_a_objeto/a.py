# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# A) Faça um programa que imprima os números no intervalo
# entre 1 e 100. Os números devem ser apresentados na
# horizontal.

import os


class Contador:
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
    
    def printar(self, valor_inicial, valor_limite, outras_coisas):
        pass
    
class PrintarNumeros(Contador):
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
    
    def printar(self):
        for i in range(self.valor_inicial, self.valor_limite):
            print(f'{i}', end=' ')

os.system('cls')
            
contador = PrintarNumeros(1, 101)
contador.printar()