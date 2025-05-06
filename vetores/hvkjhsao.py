import os
os.system("clear")

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04

def calcular_irrf(salario, dependentes):
    deducao = 189.59 * dependentes
    base_calculo = salario - deducao

    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_vale_transporte(salario, optou):
    return salario * 0.06 if optou == 's' else 0.0

def calcular_vale_refeicao(valor_beneficio):
    return valor_beneficio * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

print("--- Sistema de Folha de Pagamento ---")

matricula = input("Digite a matrícula do funcionário: ")
senha = input("Digite a senha: ")

salario_base = float(input("Informe o salário base (R$): "))
vale_transporte = input("Deseja receber vale transporte? (s/n): ").strip().lower()
valor_vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
dependentes = int(input("Informe a quantidade de dependentes: "))


desconto_inss = calcular_inss(salario_base)
desconto_irrf = calcular_irrf(salario_base, dependentes)
desconto_vt = calcular_vale_transporte(salario_base, vale_transporte)
desconto_vr = calcular_vale_refeicao(valor_vale_refeicao)
desconto_saude = calcular_plano_saude(dependentes)

total_descontos = desconto_inss + desconto_irrf + desconto_vt + desconto_vr + desconto_saude
salario_liquido = salario_base - total_descontos


print(f"Matrícula: {matricula}")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
print(f"Desconto Plano de Saúde: R$ {desconto_saude:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")