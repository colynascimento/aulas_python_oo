# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 20/08/2024
# Aula 001 - Fundamentos da Programação Orientada a Objetos: Método Construtor __init__

import os


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        
# Solicitando entrada de dados do usuário
print('-' * 70)

os.system('cls')

numero_conta = input('Digite o número da conta: ')
nome_titular = input('Digite o nome do titular: ')
saldo = float(input('Digite o saldo inicial: '))
agencia = input('Digite a agência: ')
tipo_conta = input('Digite o tipo de conta: ')

# Criando um objeto da classe ContaBancaria com os dados fornecidos pelo usuário
conta = ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

# Acessando e imprimindo atributos do objetos
print('-' * 70)
print('\nInformações da Conta Bancária:')
print('=' * 70)
print(f'Número da Conta: {conta.numero_conta}')
print(f'Nome do Titular: {conta.nome_titular}')
print(f'Saldo: {conta.saldo}')
print(f'Agência: {conta.agencia}')
print(f'Tipo de Conta: {conta.tipo_conta}')
print('-' * 70)