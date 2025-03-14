import os
os.system("clear")

par = 0
impar = 0



for i in range(5):
    numero = int(input("Digite seu números: "))
    if numero % 2 == 0:
        par += 1 
    else:
        impar += 1


print(f"Ímpares:{impar} ")
print(f"Par:{par} ")        



