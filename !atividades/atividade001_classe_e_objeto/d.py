# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 03/09/2024
# Atividade 001 - Classe e Objeto

# D) Faça um programa que receba e divida 2 números. A
# saída da divisão precisará ser formatada com 4 casas
# decimais.

import os


class Divisao:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def dividir(self):
        quociente = self.dividendo / self.divisor
        return quociente

    def formatar_resultado(self, quociente):
        return f'{quociente:.4f}'

os.system('cls')

dividendo = float(input('Digite o dividendo: '))
divisor = float(input('Digite o divisor: '))

divisao = Divisao(dividendo, divisor)
resultado = divisao.dividir()

resultado_formatado = divisao.formatar_resultado(resultado)

print(f'O resultado da divisão é {resultado_formatado}')