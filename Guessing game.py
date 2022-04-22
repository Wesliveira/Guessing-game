import time
print('-----------------------------------------')
print('***BEM-VINDO AO JOGO DE ADIVINHAÇÃO!***')
print('-----------------------------------------')

time.sleep(2)

print('TE DESAFIAMOS A ACERTAR A PALAVRA SECRETA, LETRA POR LETRA!')

time.sleep(2)
print()

print('TEM APENAS TRÊS CHANCES, ENTÃO USE-AS DA MELHOR FORMA. BOA SORTE!')

time.sleep(0.5)
print()

print('VAMOS NESSA?')

print()
secreto = "carro"
digito = []
chance = 3


while True:
    time.sleep(1)

    if chance == 0:
        print('Que pena! Você perdeu.')
        break

    letra = input('Escolha uma letra: ')

    if len (letra) > 1:
        print()
        print("Ah... Isso não vale! Digite apenas uma letra.")
        continue

    digito.append(letra)

    if letra in secreto:
        time.sleep(1)
        print()
        print(f'Você está indo bem! A letra "{letra}" existe na Palavra Secreta!')

    else:
        time.sleep(1)
        print()
        print(f'Ah não... :( A letra "{letra}" não existe na Palavra Secreta.')
        digito.pop()

    secret_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digito:
            secret_temp += letra_secreta
        else:
            secret_temp += '*'
            
    if secret_temp == secreto:
        print()
        print(f'WOW \o/ Você realmente manda muito bem. A Palavra Secreta era: "{secret_temp}"')
        break
    else:
        print()
        print(f'A Palavra Secreta por enquanto está assim: "{secret_temp}"')

    if letra not in secreto:
        chance -= 1
        print(f'Você ainda tem: {chance} chances.')
        print() 