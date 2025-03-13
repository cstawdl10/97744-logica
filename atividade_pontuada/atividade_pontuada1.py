import os

os.system("clear")

primeiro_numero = int(input("Digite seu primeiro número: "))
segundo_numero = int(input("Digite seu segundo número: "))
terceiro_numero = int(input("Digite seu terceiro número: "))
resultado = int

maior = max(primeiro_numero + segundo_numero, terceiro_numero)
menor = min(primeiro_numero + segundo_numero, terceiro_numero)

if primeiro_numero + segundo_numero < terceiro_numero: 

    print("A soma desses números são menores que o terceiro número.")

elif primeiro_numero + segundo_numero == terceiro_numero:
    print("A soma desses números são iguais que o terceiro número.")

else: 
    print("A soma dos dois primeiros números são maiores do que o terceiro número.")



print()
