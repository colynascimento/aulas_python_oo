# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# c) Faça um programa que peça 4 notas, após a entrada de
# dados calcular a média das notas digitadas.

import os


class MediaAluno:
    def __init__(self, avaliacao_1, avaliacao_2, avaliacao_3, avaliacao_4):
        self.avaliacao_1 = avaliacao_1
        self.avaliacao_2 = avaliacao_2
        self.avaliacao_3 = avaliacao_3
        self.avaliacao_4 = avaliacao_4
    
    def calcular_media(self):
        return (self.avaliacao_1 + self.avaliacao_2 + self.avaliacao_3 + self.avaliacao_4) / 4
    
    def validar_numero(self):
        try:
            self.avaliacao_1 = float(self.avaliacao_1) 
            self.avaliacao_2 = float(self.avaliacao_2) 
            self.avaliacao_3 = float(self.avaliacao_3)
            self.avaliacao_4 = float(self.avaliacao_4)
            return True
        except ValueError:
            return False    
    
import os

os.system('cls')

while True:
    print('_' * 60)
    print('Bem vindo ao programa!')
    print('Vamos calcular a média das notas de um aluno.')
    print('_' * 60)
    
    avaliacao_1 = input('Insira a nota da avaliação 1: ')
    avaliacao_2 = input('Insira a nota da avaliação 2: ')
    avaliacao_3 = input('Insira a nota da avaliação 3: ')
    avaliacao_4 = input('Insira a nota da avaliação 4: ')

    media_aluno = MediaAluno(avaliacao_1, avaliacao_2, avaliacao_3, avaliacao_4)

    if not media_aluno.validar_numero():
        
        os.system('cls')
        
        print('Entrada inválida! Por favor, insira apenas números.')
        continue
    
    print('_' * 60)
    print(f'Media do aluno: {media_aluno.calcular_media()}')
    break
    
print()
print('Fim do programa')
print()
