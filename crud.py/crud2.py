import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: str
   
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")
        print()
       
   
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        cargo=input("Cargo: "),
        salario=input("Salário: ")
    )
    lista.append(funcionario)

    print("Funcionário adicionado com sucesso.")
   
def mostrar(lista):
    if verificar_lista_vazia(lista):
        return
   
    print("\n= Lista de funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()
       
def atualizar(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False
   
    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os dados do funcionário = ")
            funcionario.nome=input("Nome: "),
            funcionario.cpf=input("CPF: "),
            funcionario.cargo=input("Cargo: "),
            funcionario.salario=input("Salário: ")
            encontrado = True
            break
   
    if not encontrado:
        print(f"\nO funcionário com o nome {funcionario.nome} não foi encontrado.")
       
    mostrar(lista)
   
def excluir(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_excluir = input("Digite o nome do funcionário: ")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_excluir:
            lista_funcionarios.remove(funcionario)
            print("Funcionário excluído com sucesso.")
        else:
            print("Funcionário não encontrado.")
def salvar_arquivo(lista):
    nome_arquivo = "funcionarios.csv"
    with open(nome_arquivo,"a") as arquivo:
        for funcionario in lista:
            arquivo.write(f"Nome: {funcionario.nome}\n{funcionario.cpf}\n{funcionario.cargo}\n{funcionario.salario}")
lista_funcionarios = []

while True:
    print("= Gerenciador de nomes =")
    print("1 - Adicionar")
    print("2 - Mostrar nomes")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")
   
    opcao = str (input("Digite uma das opções acima: "))
   
    match opcao:
        case "1":
            adicionar(lista_funcionarios)
        case "2":
            mostrar(lista_funcionarios)
        case "3":
            atualizar(lista_funcionarios)
        case "4":
            excluir(lista_funcionarios)
        case "5":
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 1:
        time.sleep(2.5)
    os.system("cls || clear")

