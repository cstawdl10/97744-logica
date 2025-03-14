import os 
os.system("clear")

notas = 0
media = 0


for i in range (4):
    notas = int(input("Digite suas notas: "))
    media += notas / 4
   
 

print(f"Sua média é:{media}")