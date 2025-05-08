import os
os.system("cls || clear")

from dataclasses import dataclass 


@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Totó", 4, 7.8)
pet2 = Pet("Tubarão",6, 9.2)

print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}anos.")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}anos.")
print(f"Nome: {pet1.nome}, idade: {pet1.idade}anos, peso:{pet1.peso}.")
print(f"Nome: {pet2.nome}, idade: {pet2.idade}anos, peso:{pet2.peso}.")
