import os
os.system("clear")
from dataclasses import dataclass


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
        
pessoa1 = Pessoa(
    input("Digite seu nome: "),
    input("Digite sua idade: "),
    input("Digite o logradouro: "),
    input("Digite o número: "),
    

)
pessoa1.exibir_dados()

