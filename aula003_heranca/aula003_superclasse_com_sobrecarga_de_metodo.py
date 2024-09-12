# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/09/2024
# Aula 003 - Herança: Método de Super Classe com Sobrecarga de Método

import os


class ClassePai:    # Super Classe
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    
    # Método que vai ser sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a * self.b
        print(f'Este cálculo está sendo realizado')
        print(f'pelo Método da Classe Pai!')
        print(f'O resultado da soma de {self.a} e {self.b} = {resultado}')
        
        
class ClasseFilha(ClassePai):   # Classe Derivada
    # Método construtor
    def __init__(self, a, b):
        super().__init__(a, b) # Chama o construtor de classe pai
        # Não é necessário redefinir a variável self.a e self.b,
        # pois já foram inicializadas pelo construtor da classe pai
        
    # Sobrecarga de Método
    def metodo_classe(self):
        # Primeiro, executa o método da classe pai
        super().metodo_classe()
        # Depois, executa o método da classe filha
        resultado = self.a + self.b
        print(f'O resultado da soma na Classe Filha é: {resultado}')
        
# Programa principal
teste = ClasseFilha(1, 2)
print(teste.metodo_classe())