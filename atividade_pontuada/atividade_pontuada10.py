import os
os.system ("clear")
print(""" 
==========POSTO DE COMBUSTIVEL PREÇOS==========

A = Álcool  3.79R$
G = Gasolina 6.59R$ """)


combustivel = input("Digite o tipo de combustivel que deseja abastecer o seu veículo: ").upper()
litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
os.system ("clear") 


if combustivel == "A":
    preço = 3.79
    tipo = "Álcool"

elif combustivel == "G":
    preço = 6.59
    tipo = "Gasolina"

match combustivel:
    case "A":
        if litros <= 25:
            desconto = preço *0.02
        else:
            desconto = preço * 0.04
    case "G":
        if litros <= 25:
            desconto = preço * 0.03
        else:
            desconto = preço * 0.05
    case _:
        print("Invalido")
        exit()
            
valor = preço * litros
valorfinal = valor - desconto



print(f"O valor total a ser pago é de {valorfinal:.2f} no(a) {tipo}")
print(f"Você abasteceu {litros}L")
         