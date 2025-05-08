import os
from dataclasses import dataclass

os.system("clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"\nNome: {self.idade}")
        print(f"\nEndereço: {self.endereco.logradouro}, número:{self.endereco.numero}")
        

endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta", 44, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B", 23)
pessoa2 = Pessoa("Judite", 44, endereco2)
pessoa2.exibir_dados()
