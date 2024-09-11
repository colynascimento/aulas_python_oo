# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# L) Faça um programa que verifique se o usuário e senha
# estão inseridos em um banco de dados (fake). O usuário
# só terá acesso se digitar os dados corretos e, assim,
# sair do laço.

import os

dados_login = {'ColyChan': 'bolo_de_morango', 'RelampagoMarquinhos': '321katchau'}

class BancoDeDados:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def verificar_usuario(self, usuario, senha):
        pass
            
    def verificar_senha(self, usuario, senha):
        pass
    
class Login(BancoDeDados):
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def verificar_usuario(self):
        verificar_usuario = bool()

    