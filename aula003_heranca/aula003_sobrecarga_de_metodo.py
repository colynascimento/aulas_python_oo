# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 11/09/2024
# Aula 003 - Herança: Sobrecarga de Método

import os


class ClassePai:    # Super Classe
    # Método Construtor
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    # Para sobrecarregar
    # Vai ser usada para soma 2 números
    def metodo_classe(self, a, b):
        pass
    
    
class ClasseFilha:  # Classe Derivada
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # Sobrecarga de Método        
    def metodo_classe(self):
        return self.a + self.b
    
    
# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()