# cria um dicionario de vendas de tecnotogia com chave e valor (string e intreiro) imprimindo a quantidade de unidade vendas de cada item.
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

for chave in vendas_tecnologia: #para cada chave no dicionario vendas_tecnologia imprima a chave e o valor 
    print(f"{chave}: {vendas_tecnologia[chave]}: unidades ") #imprimindo a chave e o valor da chave no dicionario vendas tecnologia
    
    
total_notebooks = 0 #criando uma variavel total notebook com valor 0
for chave in vendas_tecnologia: #para cada chave no dicionario vendas_tecnologia
    if 'notebook' in chave: #se a chave notebook estiver no dicionario
        total_notebooks += vendas_tecnologia[chave] #adiciona o valor da chave no total de notebooks
print(f"{chave}: {total_notebooks}: unidades ") #imprimindo a chave e valor