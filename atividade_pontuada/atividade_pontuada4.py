import os

os.system("clear")


print("""
        ==============================Menu================================
 Código                    \tAté 5kg              \tAcima de 5kg
    1  Morango              R$ 2,50 kg              R$ 2,20 kg
    2  Maçã                 R$ 1,80 kg              R$ 1,50 kg




""")


kg_maca = float(input("Quantos kg de maçã você deseja ?: "))
morango = float(input("Quantos kg de morango você deseja ?: "))
preco_morango = float
valor_com_desconto = float

if morango > 5:
    preco_morango = 2.20
elif morango > 8 and 50.00:
    preco_morango = 2.20
    desconto = preco_morango * 0.10
    valor_com_desconto = preco_morango - desconto
else:
    preco_morango = 2.50    

valor_total = preco_morango * morango 
desconto = preco_morango * 0.10
valor_com_desconto = preco_morango - desconto


print()
print(f"\nValor total das compras: {valor_total: .2f}")
print(f"Valor com desconto: {valor_com_desconto}")
print(f"Valor total com desconto:{desconto}")