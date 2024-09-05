# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# J) Faça um programa com entrada de dados para calcular
#  o perímetro de um retângulo. 

import os


class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def calcular_perimetro(self):
        perimetro = self.comprimento * 2 + self.altura * 2
        return perimetro
    
os.system('cls')

comprimento_retangulo = int(input('Digite o comprimento do retângulo: '))
altura_retangulo = int(input('Digite a altura do retângulo: '))

retangulo = Retangulo(comprimento_retangulo, altura_retangulo)
perimetro = retangulo.calcular_perimetro()

print(f'O perímetro do retângulo é: {perimetro}')