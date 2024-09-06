# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 05/09/2024
# Aula 002 - Diferença de Property para Get e Set padrão

import os


os.system('cls')


class MinhaClasse:
    def __init__(self, valor):
        self._atributo = valor
        
    @property
    def atributo(self):
        return self.atributo
    
    @atribuo.setter
    def atributo(self, valor):
        self._atributo = valor
        
obj = MinhaClasse(10)
# O atributo trabalha como uma variável
obj.atributo = 20 # (set)
# Saída semelhante a uma variável
print(obj.atributo) # (get)