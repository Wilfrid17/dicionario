

# Exemplo de uso do comando 'break' para interromper o loop quando i for igual a 10
for i in range(20):
    print(f"Valor de i é {i}")
    if i == 10:
        print("Parando o loop")
        break
    
    
# Exemplo de uso do comando 'continue' para pular a iteração atual quando i for par
for i in range(20):
    if i % 2 == 0:
        continue
    print(f"Valores impares são {i}")
    

# Exemplo de uso do comando 'pass', que não faz nada e apenas segue para a próxima iteração
for i in range(20):
    if i % 2 == 0:
        pass
    print(f"Valores são: {i}")