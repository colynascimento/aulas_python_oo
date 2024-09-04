# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# G) Faça um programa que converta metros em centímetros e
# milímetros.

import os


class ConversorDeMedidas:
    def __init__(self, metros):
        self.metros = metros
        
    def converter_em_centimetros(self):
        return self.metros * 100
    
    def converter_em_milimetros(self):
        return self.metros * 1000
    
os.system('cls')

medida_metros = float(input('Digite um valor em metros: '))

conversor = ConversorDeMedidas(medida_metros)
medida_centimetros = conversor.converter_em_centimetros()
medida_milimetros = conversor.converter_em_milimetros()

print(f'{medida_metros}m correspondem a {medida_centimetros}cm.')
print(f'{medida_metros}m correspondem a {medida_milimetros}mm.')