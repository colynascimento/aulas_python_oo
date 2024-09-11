# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# K) Crie um programa que pede que o usuário digite um nome
# ou uma frase, verifique se esse conteúdo digitado é um
# palíndromo ou não, exibindo em tela esse resultado.

import os


class VerificadorString:
    def __init__(self, entrada):
        self.entrada = entrada

    def vericar_palindromo(self, entrada):
        pass
    
class Palindromo(VerificadorString):
    def __init__(self, entrada):
        self.entrada = entrada
        
    def vericar_palindromo(self):
        self.entrada = entrada.replace(' ', '').lower()
        
        if self.entrada[::-1] == self.entrada:
            return True
        else:
            return False
        
os.system('cls')

entrada = input('Digite uma frase: ')

verificar_string = Palindromo(entrada)

if verificar_string.vericar_palindromo():
    print(f'{entrada} é um palíndromo!')
else:
    print(f'{entrada} não é um palíndromo')