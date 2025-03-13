import os
os.system("clear") 
print("""
==========TABELA DO EMPRÉSTIMO==========
O valor total deve ser 10x o valor da renda mensal do solicitante
E a prestação não pode ser maior que 30% da renda mensal do solicitante
      """)


renda = float(input("Digite o valor da renda do solicitante: "))
emprestimo = float(input("Digite o valor do empréstimo que você deseja: "))
parcelas = int(input("Digite a quantidade de parcelas que vc deseja: "))
os.system("clear")


if emprestimo <= renda * 10 and emprestimo / parcelas <= renda * 0.30:
    print("Empréstimo aprovado")

else:
    print("Empréstimo não aprovado")
    print(f"O valor do empréstimo deve ser 10x o valor da renda mensal do solicitante {renda * 10}")
    print(f"O valor da parcela não pode ser maior que 30% da renda mensal do solicitante {renda * 0.30}")
    print(f"Valor da parcela: {emprestimo / parcelas}")
    print("Quantidade de parcelas {parcelas}")
    exit()
print(f"O valor total a ser pago é de {emprestimo:.2f} R$")
print(f"O valor de cada parcela é de {emprestimo / parcelas:.2f} R$")
print(f"O total de parcelas é de {parcelas}")