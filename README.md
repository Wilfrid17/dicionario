Dicionário que armazena os itens mais vendidos em diferentes categorias.
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

Dicionário que armazena a quantidade de vendas de produtos tecnológicos.
""" Qual foi o item mais vendido nas categorias 'livros' e 'lazer'? Quanto foi vendido de 'notebook asus' e de 'ipad'? """

Acessa o valor da chave 'notebook asus' no dicionário vendas_tecnologia e armazena em vendas.
vendas = vendas_tecnologia['notebook asus']

Substitui o valor de vendas pelo valor da chave 'ipad' no dicionário vendas_tecnologia.
vendas = vendas_tecnologia['ipad']

Exibe a quantidade de vendas do último item atribuído à variável vendas (neste caso, 'ipad').
print(f"A categoria mais vendida do notebook foi: {vendas}") print(f"A categoria mais vendida do ipad foi: {vendas}")

Acessa o valor da chave 'livros' no dicionário mais_vendidos usando o método get.
qtde_livros = mais_vendidos.get('livros')

Acessa o valor da chave 'lazer' no dicionário mais_vendidos usando o método get.
qtde_lazer = mais_vendidos.get('lazer')

Exibe o item mais vendido na categoria 'livros'.
print(f"A Categorio do livro mais vendido foi: {qtde_livros}")

Exibe o item mais vendido na categoria 'lazer'.
print(f"A Categoria do lazer mais vendida foi: {qtde_lazer}")

Verifica se a chave 'lazer' está no dicionário vendas_tecnologia usando o método get.
if vendas_tecnologia.get('lazer') == None: # Se a chave não estiver presente, exibe uma mensagem. print("O item não está no dicionário") else: # Se a chave estiver presente, exibe outra mensagem. print("O item está no dicionário")

Verifica se a chave 'copo' está no dicionário vendas_tecnologia usando o operador 'in'.
if 'copo' in vendas_tecnologia: # Se a chave estiver presente, exibe uma mensagem. print("O item está no dicionário") else: # Se a chave não estiver presente, exibe outra mensagem. print("O item não está no dicionário")
