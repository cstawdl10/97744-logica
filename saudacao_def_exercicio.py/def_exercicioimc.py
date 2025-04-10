import os 
os.system("clear")


def calcular(peso,altura):
    imc = peso / altura
    altura = altura1 * altura1




peso = float(input("Informe o seu peso: "))
altura1 = float(input("Informe sua altura: "))
if imc >= 40.0:
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    40.00 \t|OBESIDADE GRAU 3      \t|BUSQUE ASSISTÊNCIA MÉDICA IMEDIATAMENTE

          
                
          """)
elif imc >= 35.00:
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    35 A 39.99 \t|OBESIDADE GRAU 2      \t|CONSULTE UM MÉDICO PARA AVALIAÇÃO E ORIENTAÇÃO
          """)
elif imc >=30.00:
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    30 a 34.9 \t|OBESIDADE GRAU 1      \t|PROCURE A ORIENTAÇÃO DE UMA PROFISSONAL DE SAÚDE
          
                
          """)
          
elif imc >=25.00 :
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    25 a 29.9 \t|SOBREPESO        \t|CONSIDERE UMA DIETA BALANCEADA
       """)
                

elif imc >= 18.5:
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    18.5 a 24.9 \t|PESO NORMAL        \t|CONSULTE UM NUTRICIONISTA
          
                
          """)

elif imc < 18.5:
    print("""
    IMC          \t|CLASSIFICAÇÃO            \t|RECOMENDAÇÃO
    Abaixo de 18.5 \t|ABAIXO DO PESO        \t|CONSULTE UM NUTRICIONISTA
          
                
          """)
print(f"Altura: {altura1}")
print(f"Peso: {peso}")
print(f"Seu IMC: {imc:.2f}")
