# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# J) Crie um programa que realiza a contagem de 1 até 100,
# usando apenas de números ímpares, ao final do processo
# exiba na tela quantos números ímpares foram encontrados
# nesse intervalo, assim como a soma dos mesmos.

import os


class Contador:
    def __init__(self, valor_inicial, valor_final):
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def contar_impares(self, valor_inicial, valor_final):
        pass

    def somar_impares(self, valor_inicial, valor_final):
        pass

class Impares(Contador):
    def __init__(self, valor_inicial, valor_final):
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def contar_impares(self):
        contador = 0

        for numero in range(self.valor_inicial, self.valor_final + 1):
            if numero % 2 == 1:
                contador += 1

        return contador

    def somar_impares(self):
        soma = 0

        for numero in range(self.valor_inicial, self.valor_final):
            if numero % 2 == 1:
                soma += numero

        return soma

os.system('cls')

valor_inicial = int(input('Digite o número inicial do intervalo: '))
valor_final = int(input('Digite o número final do intervalo: '))

contador_impares = Impares(valor_inicial, valor_final)

print('O intervalo tem:', contador_impares.contar_impares(), 'números ímpares')
print('A soma dos ímpares é:', contador_impares.somar_impares())