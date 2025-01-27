a = True
b = False
c = True
d = False

# and -> os dois valores são verdadeiros
resultado = a and b # True and False = False
resultado = a and c # True and True = True

# or -> um dos valores é verdadeir
resultado = a or b # True
resultado = a or c # True 
resultado = b and d # False

# in verifica se algo está presente em uma estrutura
lista = [1,2,3,4]
print(1 in lista)
print(10 in lista)