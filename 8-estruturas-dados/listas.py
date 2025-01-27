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