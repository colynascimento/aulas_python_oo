# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# I) Faça um programa que receba um valor em reais, depois
# calcule quantos dólares daria para comprar com esse
# valor.

import os


class ConversorDeMoedas:
    def __init__(self, reais):
        self.reais = reais

    def converter_para_dolar(self):
        dolares = self.reais / 5.63
        return dolares
 
os.system('cls')

saldo_real = float(input('Digite o valor em reais: '))

conversor = ConversorDeMoedas(saldo_real)
saldo_dolar = conversor.converter_para_dolar()

print(F'R${saldo_real:.2f} são equivalentes a U${saldo_dolar:.2f} dólares.')