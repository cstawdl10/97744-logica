import os 
os.system("cls || clear ")

from dataclasses import dataclass

@dataclass

class Paciente:
    nome : str
    idade : str
lista_pacientes = []

for i in range(2):
    print("Digite os dados dos pacientes: ")
    paciente = Paciente(
        nome = input("Nome: "),
        idade =int(input("Idade: "))
    )
    lista_pacientes.append(paciente)

nome_arquivo = "dados_pacientes.csv"

print("Salvando dados do arquivo")
with open(nome_arquivo, "a") as arquivos_pacientes:
    for paciente in lista_pacientes:
        arquivos_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print("Salvo com sucesso.")

print("\n Acessando dados em arquivo>.")
try:
    with open(nome_arquivo, "r") as arquivos_pacientes:
        linhas = arquivos_pacientes.readlines()
        for linha in linhas:
            print(f" - {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado")