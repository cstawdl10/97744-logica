import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    
pessoa1 = Pessoa (
    input("Digite seu nome: "),
    input("Digite sua idade: "), 
    input("Digite seu peso: "),
    input("Digite sua altura: "),
)

print(f"\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso} \nAltura: {pessoa1.altura}")