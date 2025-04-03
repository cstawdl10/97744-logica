import os 
os.system("clear")

def verificar(impar_par):
    os.system("clear")
    print(f"{numero}")
    if numero % 2 == 0:
        print("Esse número é par!!!")
    else:
        print("Esse número é impar!!!")
            
            
while True:
    numero = int(input("Digite seu número: "))
    if numero == 0:
        print("ENCERRADOOO")
        break
    verificar(numero)

