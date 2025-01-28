numero_sorte = 7

for i in range(3):
    # caso a pessoa escreve um número por extenso, por exemplo, o programa quebra
    try:
        numero = int(input("Digite um número entre 1 e 15.\n"))
    except ValueError as err:
        print(err)
        print("Digite um número...\n")
        continue

    if numero == numero_sorte:
        print("Você acertou")
        break
    elif numero > numero_sorte:
        print("Você errou! Tente um número menor.\n")
    else:
        print("Você errou! Tente um número maior.\n")
