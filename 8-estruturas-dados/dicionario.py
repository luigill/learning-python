# Dicionários
# Funciona no formato chave:valor

# chave (string): valor (qualquer tipo)

dados = {
    "nome": "Lui",
    "idade": 24,
    "jogos": [{"nome":"god of war","lancamento":2018}, {"nome":"god of war ragnarok","lancamento":2022}]
}

print(dados)
print(dados["nome"])
print(dados["jogos"][0]["nome"])

# Retorna as chaves presentes no dicionário
print(dados.keys())
# Retorna as valores presentes no dicionário
print(dados.values())