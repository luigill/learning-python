# Lista
# Pode ter elementos de vários tipos, diferente de um array
# Pode-se utilizar o in em listas

minha_lista_vazia = []
minha_lista_itens = ['um','dois','tres']

# se acessa os dados na lista por índices
print(minha_lista_itens[0]) # primeiro elemento
print(minha_lista_itens[-1]) # último elemento
print(minha_lista_itens[1]) # elemento na posição 1

# tamanho da lista
print(len(minha_lista_itens))

# slice de lista
# pega a partir do elemento 1 até o elemento 2
# intervalo fechado:aberto
print(minha_lista_itens[1:2])

# start:stop:step
# vai de 2 em 2
print(minha_lista_itens[::2])

# invertendo uma lista
print(minha_lista_itens[::-1])

# Métodos das listas
notas = []
notas.append(7.2) # Adiciona elemento no final da lista
notas.extend([10.0,6.7,8.0]) # Adiciona os elementos de uma lista em outra
notas = notas + [9.9,5.7] # Soma de listas resulta da união 

notas.remove(10) # Remove a primeira ocorrência da lista

soma = sum(notas) # soma todos os valores na lista


# laços de repetição em listas 
for i in notas:
    print(i)

# lista de lista
dados = [1,2,3,[10,20],[100,200]]
print(dados[4][1])