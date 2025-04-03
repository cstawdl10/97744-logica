import os 
os.system("clear")

def verificar(impar_par):
    os.system("clear")
    print(f"{numero}")
    if numero > 0:
        print("Esse número é positivo!!!")
    elif numero == 0:
        print("Esse número é neutro")
    else:
        print("Esse número é Negativo!!!")
            
            
while True:
    try:
        numero = input("Digite seu número: ")
        if numero != "e":
            numero = int(numero)
            verificar(numero)
        else:
            print("ENCERRADOOO")
            break
    except ValueError:
        print("Opção inválida...")    

