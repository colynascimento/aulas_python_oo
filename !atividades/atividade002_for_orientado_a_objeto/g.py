# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# G) Faça um programa que calcule os números primos em um
# intervalo pré-determinado pelo usuário.

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
                if (numero % i == 0) and (numero != i):
                    primo = False
                    break
            
            if primo:
                print(numero, end=' ')

os.system('cls')

valor_inicial = int(input('Digite o número inicial do intervalo: '))
valor_final = int(input('Digite o número final do intervalo: '))

contador = PrintarPrimos(valor_inicial, valor_final)

contador.printar()