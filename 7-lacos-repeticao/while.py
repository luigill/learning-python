count = 1

# enquanto o valor, executa
while count <= 10:
    print(count)
    count += 1


while True:
    senha = input("Entre com a senha: ")
    if senha == "senha":
        break # Sai do laço
    elif senha == 'senh': 
        continue # Continua no laço, mas do começo
print("Saí do laço")