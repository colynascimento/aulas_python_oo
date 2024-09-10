# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# F) Faça um programa que imprima os números primos entre
# 0 e 100.

import os


class Contador:
    def __init__(self, valor_minimo, valor_limite):
        self.valor_minimo = valor_minimo
        self.valor_limite = valor_limite

    def printar(self, valor_minimo, valor_limite):
        pass

class PrintarPrimos(Contador):
    def __init__(self, valor_minimo, valor_limite):
        self.valor_minimo = valor_minimo
        self.valor_limite = valor_limite

    def printar(self):
        primo = bool()

        for numero in range(self.valor_minimo, self.valor_limite + 1):
            if numero == 1:
                primo = False
            else:
                primo = True

            for i in range(2, numero):
                if (numero % i == 0) and (i != numero):
                    primo = False
                    break

            if primo:
                print(numero, end=' ')
        
os.system('cls')

contador = PrintarPrimos(1, 100)

contador.printar()