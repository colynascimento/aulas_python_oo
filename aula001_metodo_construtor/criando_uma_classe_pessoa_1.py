# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 20/08/2024
# Aula 001 - Fundamentos da Programação Orientada a Objetos: Método Construtor __init__

import os


class Pessoa:
    def __init__(self, nome, cpf, nascimento, cep, cidade, estado):
        # Inicializando os atributos
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

# Solicitando entrada de dados do usuário
os.system('cls')

print('-' * 70)

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
nascimento = input('Digite o ano de nascimento: ')
cep = input('Digite o CEP: ')
cidade = input('Digite a cidade: ')
estado = input('Digite o estado: ')

# Criando um objeto da classe Pessoa com os dados fornecidos pelo usuário
pessoal = Pessoa(nome, cpf, nascimento, cep, cidade, estado)

# Acessando e imprimindo os atributos do objeto
print('-' * 70)
print('\nInformações da Pessoa:')
print('=' * 70)
print(f'Nome: {pessoal.nome}')
print(f'CPF: {pessoal.cpf}')
print(f'Ano de Nascimento: {pessoal.nascimento}')
print(f'CEP: {pessoal.cep}')
print(f'Estado: {pessoal.estado}')
print('-' * 70)