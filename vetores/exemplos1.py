import os
os.system("clear")

lista_de_compras = []
QUANTIDADE = 3  

print("=LISTA DE COMPRAS=")
for i in range(QUANTIDADE):
    item = input(f"digite o {i+1} item para lista: ")
    lista_de_compras.append(item)

print("\n=ITENS DA LISTA=")
for i, item in enumerate(lista_de_compras,start=1):
    print(f"{i} item: {item}")
    