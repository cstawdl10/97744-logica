import os 
os.system("clr || clear")
idade = int
sexo = str
salario = float
while True:
    print("""   
 Código | Descrição 
    1   | Adicionar Pessoa
    2   | Exibir Resultados  
    3   | Sair       
    
   
      
      
""")
    codigo = int(input("Digite sua opção desejada: "))

    match codigo:
        case 1:
            input("Digite a idade: ")
            input("Digite o sexo: ")
            input("Digite o salário: ")
            os.system("clear")
        case 2:
            print(f"{idade}")
            print(f"{sexo}")
            print(f"{salario}")
        case 3:
            exit()
        case _:
            print("Opção inválida. ")
            os.system("clear")





