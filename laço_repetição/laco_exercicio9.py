import os
os.system("clear")

import os 
os.system("clear")

login_correto = "putaria"
senha_correta = "sexo"
contador = 0


while True:
        login = input("Login: ")
        senha = input("Senha: ")
        if login == login_correto and senha == senha_correta:
            print()
            print("===========Seja bem-vindo============\n")
            break
        else:
            print("Acesso negado\n")
            contador += 1
            if contador == 3:
                 print("=============Números de tentativas acima do permitido============\n")
                 break
          