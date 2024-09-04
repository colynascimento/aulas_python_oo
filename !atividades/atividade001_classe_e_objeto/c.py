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
    
import os

os.system('cls')

avaliacao_1 = int(input('Insira a nota da avaliação 1: '))
avaliacao_2 = int(input('Insira a nota da avaliação 2: '))
avaliacao_3 = int(input('Insira a nota da avaliação 3: '))
avaliacao_4 = int(input('Insira a nota da avaliação 4: '))

# Tirar o int depois e fazer uma validação dentro da classe

media_aluno = MediaAluno(avaliacao_1, avaliacao_2, avaliacao_3, avaliacao_4)


print(f'Media: {media_aluno.calcular_media()}')