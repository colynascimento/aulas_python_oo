# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# B) Evolua o programa anterior para um código que pergunte
# ao usuário qual o intervalo que ele deseja ver  impresso.

import os


class Contador:
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
    
    def printar(self, valor_inicial, valor_limite):
        pass
    
class PrintarNumero(Contador):
    def __init__(self, valor_inicial, valor_limite):
        self.valor_inicial = valor_inicial
        self.valor_limite = valor_limite
    
    def printar(self):
        for i in range(self.valor_inicial, self.valor_limite + 1):
            print(f'{i}', end=' ')       
        
    def validar_numero(self):
        try:
            self.valor_inicial = int(self.valor_inicial) 
            self.valor_limite = int(self.valor_limite) 
            return True
        except ValueError:
            return False    
        
os.system('cls')

while True:
    valor_inicial = input('Digite o número inicial: ')
    valor_limite = input('Digite o valor final: ')
                
    contador = PrintarNumero(valor_inicial, valor_limite)

    if not contador.validar_numero():
        os.system('cls')
        
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
        continue


    os.system('cls')

    contador.printar()
    break