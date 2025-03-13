import os 

os.system("clear")


primeiro_numero = int(input("Digite seu primeiro número: "))
print()

segundo_numero = int(input("Digite seu segunda número: "))
print()

media = (primeiro_numero + segundo_numero) / 2
soma = (primeiro_numero + segundo_numero)
multiplicaçao = (primeiro_numero * segundo_numero)
maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)






print("A média: ", media)
print("A Soma: ", soma)
print("A sua multiplicação: ", multiplicaçao)

if primeiro_numero == segundo_numero:
    print("Os números são iguais")
else:
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")    
