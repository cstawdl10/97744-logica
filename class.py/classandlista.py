import os
os.system("clear")

from dataclasses import dataclass


@dataclass
class Cliente: 
    nome: str
    email: str
    telefone: str

lista_clientes = []
quantidade_clientes = 2 

print("Informe os dados so cliente ")
for i in range (quantidade_clientes):
    cliente = Cliente(
        nome = input("Nome: "),
        email=input("E-mail: "),
        telefone = input("Telefone: "),
    )
    lista_clientes.append(cliente)
    print()

print("\n= Exibindo dados clientes =")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")