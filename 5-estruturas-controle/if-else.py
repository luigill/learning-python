idade = int(input("Digite sua idade\n"))

# If Else
if idade < 18:
    print("Você não pode beber ainda...")
elif idade > 90:
    print("Cuidado, você tem certa idade")
else:
    print("Você é maior de idade!")


if 18 <= idade <= 90:
    print("Maior de idade")
elif idade >= 90:
    print("Pessoa mais velha")
else:
    print("Muito jovem")