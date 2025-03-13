import os

os.system("clear")

maca = int(input("Quantas maçãs o senhor vai querer ?: "))




if maca < 12 :
    preco_maca = 1.30 
else:
    preco_maca = 1.00

valor_total = maca * preco_maca

print()
print(f"Valor total de compra R$ {valor_total: .2f}")
