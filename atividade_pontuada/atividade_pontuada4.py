import os

os.system("clear")


kgmorango = float(input("Digite quantos KG de morangos você ira levar: "))
kgmaca = float(input("Digite quantos KG de maçãs você ira levar: "))
if kgmorango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kgmaca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

valormorango = kgmorango * preco_morango
valormaca = kgmaca * preco_maca
valorkgtotal = valormorango + valormaca
kgtotal = kgmorango + kgmaca


if valorkgtotal >= 50 or kgtotal >= 8:
    desconto = valorkgtotal * 0.10
    valorkgtotal = valorkgtotal - desconto
print(f"O valor total a ser pago é de R${valorkgtotal:.2f}")
print(f"Você comprou {kgtotal} KG de frutas")
