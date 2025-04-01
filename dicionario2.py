""" dicionario = {}

   dicionario[chave] = valor

   outra opção:

    dicionario.update({chave: valor, chave: valor})
"""""
#criando um dicionario com 3 itens chave e valor (string e inteiro) de determinado trimeses com o lucro gerado por cada mes durante essse ano.
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
#adicionando 1 item
lucro_1tri['abril'] = 88000 #adicionando um  item
print(lucro_1tri) #imprimindo o item no dicionario

#adicionando vários itens ou um dicionário a outro
lucro_1tri.update(lucro_2tri) 
print(lucro_1tri)
#adicionando um item já existente (manualmente ou pelo update)
lucro_1tri['abril'] = 100000
print(lucro_1tri)

#Modificar itens:
#Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.
#dicionario[chave] = valor
#Vamos modificar o lucro de fevereiro:
#(Lembrando: caso o item não exista, ele vai criar o item no dicionário)

lucro_fev = 85000
lucro_1tri['fevereiro'] = lucro_fev
print(lucro_1tri)

 #Remover itens:
#del dicionario[chave]
#ou então
#valor = dicionario.pop(chave)
#mas cuidado com:
#del dicionario<br>    ->    que é diferente de dicionario.clear()

#removendo o mês de junho
del lucro_1tri['junho']


#obs: o del também funciona para listas, caso queira usar
#del lista[i]

funcionarios = ['João', 'Lira', 'Maria', 'Ana', 'Paula']
print(funcionarios)
