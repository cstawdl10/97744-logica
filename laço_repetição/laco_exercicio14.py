import os
os.system("clear")

par = 0
impar = 0
media = 0
mediap = 0
somag = 0
somap = 0
quantidade_geral = 0


while True:
    numero = int(input("Digite seu números: "))
    if numero <= 0:
            break
            
    if numero % 2 == 0:
        par += 1
        somap += numero
        
        
    else:
        impar += 1 
        
        
    somag += numero
    quantidade_geral += 1

if quantidade_geral > 0:
    mediap = somap / par
    media = somag / quantidade_geral
            
             
    print(f"Ímpares:{impar} ")
    print(f"Par:{par} ")  
    print(f"Média pares:{mediap}")      
    print(f"Médias gerais:{media}")
else:
     print("Não foram informados números necessários para a operação.")          