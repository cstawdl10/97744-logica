import os
import time 
os.system("clr || clear")


media_salario_grupo = 0
soma_salario = 0
contador = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0
while True:
    print("""   
 Código | Descrição 
    1   | Adicionar Pessoa
    2   | Exibir Resultados  
    3   | Sair       
    
   
      
      
""")
    opcao = int(input("Digite sua opção desejada: "))

    match opcao:
        case 1:
            idade = int (input("Digite a idade: "))
            sexo = input("Digite o sexo com 'M' ou 'F': ").upper()
            salario = int(input("Digite o salário:"))
            contador += 1
            soma_salario += salario

            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
            os.system("clear")
        case 2:
            if contador > 0: 
                media_salario_grupo = soma_salario / contador
                print(f"Média de salário do grupo: {media_salario_grupo}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Mulheres com Salário acima de 5mil: {mulheres5k}")
            else: 
                print("Não existem dados para exibir.")
            
            time.sleep(3)
            os.system("clear")
        case 3:
            print("Fim")
            break
        case _:
            print("Opção inválida. ")
            time.sleep(3)
            os.system("clear")
            




