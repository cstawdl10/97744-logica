import os 
os.system("clear")



def inflacao(preco):
    if preco < 100:
        valor = preco *1.10
    else:
        valor = preco *1.20
    return valor
preco = float(input("Digite o valor do produto:"))


preco_final = inflacao(preco) 

print(f"Valor final: {preco_final}")
    
