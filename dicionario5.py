#tranformar o dicionario em tupla

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

diciionario = vendas_tecnologia.items()#Esse metodo transforma o dicionario em uma tupla com chave e valor
print(diciionario)#imprimindo o dicionario transformado em tupla

#aqui podemos fazer um unpacking da tupla para acessar a chave e o valor
for produto, quantidade in vendas_tecnologia.items():#vai percorrer o dicionario vendas_tecnologia e vai imprimir a chave e o valor
    print(f"{produto}: {quantidade} unidades")#imprimir a chave e o valor
    
#Quais produtos venderam mais de 10.000 unidades?
for produto, quantidade in vendas_tecnologia.items():  #para cada chave e valor no dicionario vendas_tecnologia
    if quantidade > 10000: #para verificar se a quantidade é maior que 10000 vai imprimir somente os produtos que venderam mais de 10000 unidades
        print(f"O produto: {produto}: venderam {quantidade} unidades") #imprimir o produto e a quantidade vendida
        
#Quais produtos venderam menos ou igual a 1000 unidades?
for produto, quantidade in vendas_tecnologia: #vai percorrer o dicionario vendas_tecnologia
    if quantidade <= 1000: #para vericar se a quantidade é menor ou igual a 1000
        print(f"O produto {produto} vendeu menos de {quantidade} unidades") #imprimir o produto e a quantidade vendida