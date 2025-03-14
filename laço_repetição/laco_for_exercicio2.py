import os 

os.system("clear")

numero = int(input("Digite o número que você deseja fazer a multiplicação: "))


print(f"TABUADA DE MULTIPLICAÇÃO DO NÚMERO {numero} ")
for i in range(1,11):
    print (f"{numero} x {i} = {i*numero}")
  
                    