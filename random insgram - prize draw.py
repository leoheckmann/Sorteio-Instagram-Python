import random
usuarios = []

def cadastro_user(nome:str):
    usuarios.extend((nome).split())
    return

def receber_user():
    random.shuffle(usuarios)
    return random.choice(usuarios)

frase1 = ("Sorteio de usuários do Instagram")
print("=~=" * 30)

print(f"\033[1;33m{frase1}")
print("\033[0;0m=~=" * 30)

users = int(input("\033[1;31mDigite 1 para cadastrar o usuário e 2 para finalizar e ir para o sorteio: "))
print(" ")

while users == 1:
    arr = (input("\033[1;33mInsira o usuário: "))

    cadastro_user(arr)

    users = int(input("\033[1;31mDigite 1 para cadastrar o usuário e 2 para finalizar: "))

if len(usuarios) > 0:
    print(f"\033[1;0mUsuários cadastrados para o sorteio: {usuarios}")
    print(f"\033[1;34mO ganhador do sorteio foi: {receber_user()}")







