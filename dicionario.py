mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}
# Dicionário que armazena os itens mais vendidos em diferentes categorias.

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
# Dicionário que armazena a quantidade de vendas de produtos tecnológicos.

"""
Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
Quanto foi vendido de 'notebook asus' e de 'ipad'?
"""

qtde_livros = mais_vendidos['livros']
# Obtém o item mais vendido na categoria 'livros' do dicionário `mais_vendidos`.

qtde_lazer = mais_vendidos['lazer']
# Obtém o item mais vendido na categoria 'lazer' do dicionário `mais_vendidos`.

print(f"A Categorio do livro mais vendido foi: {qtde_livros}")
# Exibe o item mais vendido na categoria 'livros'.

print(f"A Categoria do lazer mais vendida foi: {qtde_lazer}")
# Exibe o item mais vendido na categoria 'lazer'.

qtde_notebook = vendas_tecnologia['notebook asus']
# Obtém a quantidade de vendas do produto 'notebook asus' no dicionário `vendas_tecnologia`.

qtde_ipad = vendas_tecnologia['ipad']
# Obtém a quantidade de vendas do produto 'ipad' no dicionário `vendas_tecnologia`.

print(f"A categoria mais vendida do notebook foi: {qtde_notebook}")
# Exibe a quantidade de vendas do produto 'notebook asus'.

print(f"A categoria mais vendida do ipad foi: {qtde_ipad}")
# Exibe a quantidade de vendas do produto 'ipad'.