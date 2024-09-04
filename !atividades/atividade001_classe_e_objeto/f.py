# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# F) Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

import os


class Multiplicacao:
    def __init__(self, numero):
        self.numero = numero
        
    def calcular_dobro(self):
        return self.numero * 2
        
    def calcular_triplo(self):
        return self.numero * 3
    
os.system('cls')

entrada = int(input('Digite um número: '))

numero = Multiplicacao(entrada)
dobro = numero.calcular_dobro()
triplo = numero.calcular_triplo()

print(f'O dobro de {entrada} é {dobro}')
print(f'O triplo de {entrada} é {triplo}')