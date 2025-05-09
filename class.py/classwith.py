import os 
os.system("clear")

from dataclasses import dataclass

@dataclass 
class Cliente:
    nome:str
    email:str
    telefone:str
lista_clientes = []
QUANTIDADE_CLIENTES = 2 

for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome=input("Nome: "),
        email=input("Email: "),
        telefone=input("Telefone: "),
)
    lista_clientes.append(cliente)
    print()
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print()
print("=Salvando dados do clientes =")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open(nome_arquivo, "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome},{cliente.email,},{cliente.telefone}\n")