import os
os.system("clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular
def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular
def dividir(n1, n2):
    return n1 / n2 
     
def multiplicar(n1, n2):
    return  n1 * n2
    

n1 = int(input("Digite seu primeiro número: "))

n2 = int(input("Digite seu segundo número: "))

soma = somar(n1, n2)
sub = subtrair(n1, n2)
div = dividir(n1, n2)
mult = multiplicar(n1, n2)

print (f"Soma: {soma}")
print (f"Subtração: {sub}")
print (f"Multiplicação: {mult}")
print (f"Divisão: {div}")