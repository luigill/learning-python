# Funções são trechos reutilizáveis de código que resolvem um problema específico.

# parâmetros são valores esperados pela função para executar
# pode-se definir valores padrões para os parâmetros
def soma_numeros(a, b = 0):
    # Docstring -> Explica a função
    """ Essa função soma dois números"""
    return a + b

# número indefinido de parâmetros
def soma(*args):
    total = 0
    for i in args:
        total += i
    return total


# argumentos são passados como parâmentros da função
print(soma_numeros(10, 20))
