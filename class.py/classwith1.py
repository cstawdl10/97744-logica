import os 
os.system("clear")

from dataclasses  import dataclass
lista_carros = []


@dataclass
class Carro:
    marca:str
    modelo:str
    categoria:str
    preco:float
    
    def exibir_resultados(self):
          for i in range(2):
            print(f"A marca do carro: {self.marca}")
            print(f"O modelo do carro: {self.modelo}")
            print(f"A categoria do carro: {self.categoria}")
            print(f"O preço do carro: {self.preco}")

for i in range(2):
    carros = Carro(
    input("Digite a marca do carro: "),
    input("Digite o modelo do seu carro: "),
    input("Digite a categoria do seu carro: "),
    input("Digite o preço do seu carro: "),
    )
    lista_carros.append(carros) 
os.system("clear")


carros.exibir_resultados()

print("=Salvando dados do clientes =")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open(nome_arquivo, "w") as arquivo:
        arquivo.write(f"{carros.marca},{carros.modelo,},{carros.categoria},{carros.preco}\n")
