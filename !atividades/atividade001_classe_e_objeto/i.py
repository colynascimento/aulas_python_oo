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
    