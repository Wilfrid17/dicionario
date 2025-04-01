# Este código demonstra o uso de um dicionário em Python.
# Um dicionário é uma estrutura de dados que armazena pares de chave-valor.
# Cada chave é única e pode ser usada para acessar o valor correspondente.

# Exemplo de dicionário:
dict = {
     'nome': 'Simplifica',  # 'nome' é a chave, 'Simplifica' é o valor
    'linguam': 'python',   # 'linguam' é a chave, 'python' é o valor
    'versão': 3.12,        # 'versão' é a chave, 3.12 é o valor
    'ambiente': 'Windows', # 'ambiente' é a chave, 'Windows' é o valor
     'ativo': True          # 'ativo' é a chave, True é o valor
}

# Para acessar um valor específico, você pode usar a chave:
# print(dict['nome'])  # Saída: Simplifica

# Para iterar sobre todas as chaves e valores do dicionário, usamos o método items():
# O loop abaixo percorre cada par chave-valor no dicionário e imprime ambos.
for chave, valor in dict.items():
    print(chave, valor)  # Exemplo de saída: nome Simplifica, linguam python, etc.