# só escreve no arquivo = sobrescreve o conteúdo
# arquivo = open("arquivo.txt", 'w')

# leitura e escrita = adiciona no arquivo
arquivo = open("arquivo.txt", 'a')

arquivo.write("mensagem")

arquivo.close()

# garante que o arquivo vai ser fechado
# útil também para banco de dados
with open("arquivo.txt", 'r') as file:
    conteudo = file.read()