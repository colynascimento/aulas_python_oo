# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# E) Faça um programa que some a quantidade de números
# pares encontrados no intervalo entre 0 e 100.

import os


class Operacoes:
    def __init__(self, valor_minimo, valor_limite):
        self.valor_minimo = valor_minimo
        self.valor_limite = valor_limite

    def somar(self, valor_minimo, valor_limite):
        pass

class SomarNumeros(Operacoes):
    def __init__(self, valor_minimo, valor_limite):
        self.valor_minimo = valor_minimo
        self.valor_limite = valor_limite

    def somar(self):
        resultado = 0

        for i in range(self.valor_minimo, self.valor_limite):
            if i % 2 == 0:
                resultado += i

        return print(resultado)
    
os.system('cls')

resultado = SomarNumeros(0, 101)

resultado.somar()