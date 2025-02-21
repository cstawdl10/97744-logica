import os

os.system("clear")


primeiro_numero = int(input("Digite o seu primeiro número: "))
segundo_numero = int(input("Digite seu segundo número: "))
terceiro_numero = int(input("Digite seu terceiro número: "))


maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")