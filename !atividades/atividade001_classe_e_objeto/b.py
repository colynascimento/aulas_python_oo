# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 02/09/2024
# Atividade 001 - Classe e Objeto

# B) Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

import os
from datetime import datetime


class Idade:
    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def calcular(self):
        hoje = datetime.now()
        data_nascimento = self.data_nascimento
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        self._idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

        return self._idade
    
    def validar_data(self):
        try:
            datetime.strptime(self.data_nascimento, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    
os.system('cls')

while True:
    print('_' * 60)
    print('\nSeja bem-vindo ao programa!')
    print('Vamos verificar sua idade.')
    print('_' * 60)
    
    data_nascimento = input('Insira sua data de nascimento (DD/MM/YYYY): ')
    
    idade = Idade(data_nascimento)
    
    if idade.validar_data():
        print(f'Sua idade é {idade.calcular()}.')
        break
    else:
        os.system('cls')
        print('Entrada inválida! Digite uma data no formato DD/MM/YYYY\n')
        
print('_' * 70)
print('\nFim do programa')
print()