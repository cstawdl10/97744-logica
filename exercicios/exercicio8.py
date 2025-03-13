import os
os.system("clear")

primeiro_numero = int(input("Digite seu primeiro número: "))
segundo_numero = int(input("Digite seu Segundo numéro: "))
operacao = (input("Digite sua operação desejada: "))

match operacao:
    case "+": 
        resultado = primeiro_numero + segundo_numero    
    case "/": 
        resultado = primeiro_numero / segundo_numero    
    case "-": 
        resultado = primeiro_numero - segundo_numero    
    case "*": 
        resultado = primeiro_numero * segundo_numero   

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Operação: {operacao}") 
print(f"Segundo número:{segundo_numero}")
print(f"Resultado: {resultado: .2f}")        