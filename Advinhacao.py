import random
import sys

# Para usar cores no terminal (funciona em muitos terminais):
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Reseta a cor
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def jogar():
    print(f"{bcolors.HEADER}Bem-vindo ao Jogo da Adivinhação!{bcolors.ENDC}")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input(f"{bcolors.OKCYAN}Digite seu palpite (1-100): {bcolors.ENDC}"))
        except ValueError:
            print(f"{bcolors.WARNING}Por favor, digite um número válido.{bcolors.ENDC}")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"{bcolors.OKGREEN}Parabéns! Você acertou o número em {tentativas} tentativas!{bcolors.ENDC}")
            break
        elif palpite < numero_secreto:
            print(f"{bcolors.WARNING}Tente um número maior!{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}Tente um número menor!{bcolors.ENDC}")

    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
