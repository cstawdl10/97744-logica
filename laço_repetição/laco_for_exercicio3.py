import os
import time
os.system("clear")


numero = int(input("Digite o seu número para fazer a contagem: "))
os.system("clear")



print("\n=========CONTAGEM REGRESSIVA==========")
for i in range(numero,0,-1):
    print(f"{i} ")
    time.sleep(1)
print("===================FIM==================")    
