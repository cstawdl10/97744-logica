import os 
os.system("clear")

login_correto = "putaria"
senha_correta = "sexo"


for i in range(3):
        login = input("Login: ")
        senha = input("Senha: ")
        if login == login_correto and senha == senha_correta:
            print()
            print("===========Seja Bem-Vindo============\n")
            break
        else:
            print("Acesso Negado\n")
            if i == 2:
                print("Números de tentativas acima do permitido.\n")
        
