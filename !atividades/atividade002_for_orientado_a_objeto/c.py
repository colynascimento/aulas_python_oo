# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# C) Faça um programa que imprima os números no intervalo
# entre 1 e 10 em ordem inversa.

import os


class Contador:
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
 
    def printar(self, valor_inicial, valor_limite):
        pass
    
class PrintarNumero(Contador):        
    def printar(self):
        for i in range(self.valor_inicial, self.valor_limite, -1):
            print(f'{i}', end=' ')

os.system('cls')

contador = PrintarNumero(10, 0)

contador.printar()