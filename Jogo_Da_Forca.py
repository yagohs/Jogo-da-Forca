import os
digitadas = []
errada = ''
chances = 5
digitadas_erradas = []


print('===========================')
print(f'       Jogo Da Forca')
print('===========================')
print()
print('Você tem 5 Chances')
psecreta = input('Digite a Palavra Secreta:')
os.system("cls")
num = len(psecreta)
#print("\n"*38)
print('===========================')
print(f'       Jogo Da Forca')
print('===========================')
print()
print(f'A palavra secreta tem {num} Letras'.title())

while True:
    if chances <= 0:
        print('Você Perdeu!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Ahhhhhh isso não vale, digite apena uma letra")
        continue

    for letra_secreta_antiga in digitadas_erradas:
        if letra_secreta_antiga == letra:
            print(f'Essa Letra já foi DIGITADA.')
            continue

    digitadas.append(letra)

    if letra in psecreta:
        print(f'Uhuuul, a Letra "{letra}" existe na palavra secreta')
    else:
        print(f'Affs: a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()
        digitadas_erradas.append(letra)

    secreto_temporario = ''

    for letra_secreta in psecreta:

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == psecreta:
        print('Você Acertou!!')
        print(f'A Palavra Secreta é: {secreto_temporario}.')

        break
    else:
        print(f'A palavra secreta está assim:')
        print(secreto_temporario)
        print(f'-'*len(secreto_temporario))

    if letra not in psecreta:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()