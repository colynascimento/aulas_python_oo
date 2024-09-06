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
        
    def get_atributo(self):
        return self._atributo
    
    def set_atributo(self):
        self._atributo = valor
        
obj = MinhaClasse(10)
# O atributo trabalha como uma função
obj.set_atributo(20)
# Saída como função
print(obj.get_atributo())