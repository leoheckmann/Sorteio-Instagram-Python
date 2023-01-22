import random
usuarios = []

def cadastro_user(nome:str):
    usuarios.extend((nome).split())
    return

def receber_user():
    random.shuffle(usuarios)
    return random.choice(usuarios)

frase1 = ("                          Sorteio de usuários do Instagram!")
print("=~=" * 30)

print(f"\033[1;33m{frase1}")
print("\033[0;0m=~=" * 30)

users = 1

while users == 1:
    arr = (input("\033[1;33mInsira o usuário: "))

    cadastro_user(arr)

    users = int(input("""\033[1;31m   Selecione a opção!
( 1 ) \033[1;31mCadastrar outro usuário!
( 2 ) \033[1;31mSortear o ganhador!
Digite >>> """))

if len(usuarios) > 0:
    print(f"\033[1;0mUsuários cadastrados para o sorteio: {usuarios}")
    print(f"\033[1;34mO ganhador do sorteio foi: {receber_user()}")
