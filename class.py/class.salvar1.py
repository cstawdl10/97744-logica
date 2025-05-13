import os
os.system("cls")

from dataclasses import dataclass
lista_funcionarios = []
lista_clientes = []
@dataclass
class Funcionario:
    nome : str
    data_de_admissao : int
    matricula : int 
    endereco: str
    def exibir_resultados(self):
        for i in range(3):
            print(f"Nome do funcionário: {self.nome}")
            print(f"Data de adimissão: {self.data_de_admissao}")
            print(f"Matricula: {self.matricula}")
            print(f"Endereço: {self.endereco}")
            
@dataclass    
class Cliente:
    nome : str
    data_de_nascimento: int
    endereco: str
    def exibir_resultado(self):
        for i in range(3):
            print(f"Nome do cliente: {self.nome}")
            print(f"Data de nascimento: {self.data_de_nascimento}")
            print(f"Endereço: {self.endereco}")

for i in range (3):
    funcionario = Funcionario(
        input("Digite o nome do funcionário: "),
        input("Digite a data de admissão: "),
        input("Digite o número da matricúla: "),
        input("Digite o endereço: "),
    )
    lista_funcionarios.append(funcionario)        

for i in range (3):
    cliente = Cliente(
        input("Digite o nome do cliente: "),
        input("Digite a data de nascimento: "),
        input("Digite o endereço: "),
    )
    lista_clientes.append(cliente)

funcionario.exibir_resultados()
cliente.exibir_resultado()

nome_arquivo = "dados_funcionarios.csv"

print("Salvando dados do arquivo")
with open(nome_arquivo, "a") as arquivos_funcionarios:
    for funcionario in lista_funcionarios:
        arquivos_funcionarios.write(f"{funcionario.nome}, {funcionario.idade}\n")

print("Salvo com sucesso.")

print("\n Acessando dados em arquivo>.")
try:
    with open(nome_arquivo, "r") as arquivos_funcionarios:
        linhas = arquivos_funcionarios.readlines()
        for linha in linhas:
            print(f" - {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado")
    nome_arquivo = "dados_funcionarios.csv"


nomee_arquivo = "dados_clientes.csv"

print("Salvando dados do arquivo")
with open(nomee_arquivo, "a") as arquivos_clientes:
    for cliente in lista_clientes:
        arquivos_clientes.write(f"{cliente.nome}, {cliente.idade}\n")

print("Salvo com sucesso.")

print("\n Acessando dados em arquivo>.")
try:
    with open(nomee_arquivo, "r") as arquivos_clientes:
        linhas = arquivos_clientes.readlines()
        for linha in linhas:
            print(f" - {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado")
    nomee_arquivo = "dados_clientes.csv"