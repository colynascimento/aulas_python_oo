# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/09/2024
# Atividade 001 - For() Orientado a Objeto

# I) Faça um algoritmo que imprima a frase "estou em
# looping" e, em seguida, solicite ao usuário digitar uma
# letra. Caso a letra seja o “f" finalize a aplicação. Do
# contrário, imprima novamente a mesma frase até que o
# caractere “f" seja digitado.

import os


class Looping:
    def __init__(self, entrada):
        self.entrada = entrada

    def parar_loop(self, entrada):
        pass

class PararLoop(Looping):
    def __init__(self, entrada):
        self.entrada = entrada

    def parar_loop(self):
        loop = True

        while loop == True:
            if self.entrada == 'f':
                break
            else:
                print('Estou em looping!')

            self.entrada = input('Digite uma letra: ').lower()

os.system('cls')

entrada_usuario = input('Digite uma letra: ').lower()

looping = PararLoop(entrada_usuario)

looping.parar_loop()

print('-' * 50)
print('Fim do programa!')
print()