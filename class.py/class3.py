import os 
os.system("clear")

from dataclasses  import dataclass

@dataclass

class Autor:
    nome : str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    nome: str
    
    def exibir_detalhes(self):
        print(f"=Titulo do Livro: {self.titulo}\n=Ano em que foi publicado: {self.ano}")
        print(f"=Nome do autor: {self.nome}")
       

lista_clientes = []
quantidades_clientes = 2

for autor1 in range(quantidades_clientes):
    autor1 = Livro(
        input("Digite o titulo do livro: "),
        input("Digite o ano em que o livro foi publicado: "),
        input("Digite o nome do  autor: "), 
    lista_clientes.append(autor1)
)
os.system("clear")
autor1.exibir_detalhes()
