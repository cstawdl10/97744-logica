import os
os.system("clear")

while True:
    def tabuada(numero):
        print(f"O Número informado: {numero}")
        print(f"TABUADA DE MULTIPLICAÇÃO DO NÚMERO: {numero} ")
        for i in range(1,11):
            print (f"{numero} x {i} = {i*numero}")


    numero = int(input("Digite o número para efetuar a sua tabuada:"))
    tabuada(numero)
    break
    



