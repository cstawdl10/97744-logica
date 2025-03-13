import os
os.system ("clear || cls") #LIMPEZA DE TERMINAL

print(""" 
==========CORES DOS CD´s==========
1 = verde
2 = azul
3 = amarelo
4 = vermelho""")


cd = int(input("Digite o número da cor do CD que deseja comprar: "))


if cd == 1:
    preco = 10
    cor = "verde"
elif cd == 2:
    preco = 20
    cor = "azul"
elif cd == 3:
    preco = 30
    cor = "amarelo"
elif cd == 4:
    preco = 40
    cor = "vermelho"
else:
    print("Cor não encontrada")
    exit()


print(f"O CD da cor {cor} custa R$:{preco}")