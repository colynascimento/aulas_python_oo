# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# E) Faça um programa que receba um número inteiro e mostre
# o sucessor e antecessor.

import os


class Numero:
    def __init__(self, numero):
        self.numero = numero
        
    def verificar_sucessor(self):
        sucessor = self.numero + 1
        return sucessor
    
    def verificar_antecessor(self):
        antecessor = self.numero - 1
        return antecessor
    
os.system('cls')

entrada = int(input('Digite um número: '))

# tirar int e fazer validação de número

numero = Numero(entrada)
antecessor = numero.verificar_antecessor()
sucessor = numero.verificar_sucessor()

print(f'O antecessor do número {entrada} é {antecessor}')
print(f'O sucessor do número {entrada} é {sucessor}')