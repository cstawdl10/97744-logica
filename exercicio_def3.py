import os
os.system("clear")


def covertem_centimetros(numero):
    return numero *100


numero = float(input("Digite o valor em metro: "))


centimetros = covertem_centimetros(numero)

print(f"Convertendo {numero} m em centímetros é:{centimetros}cm.")