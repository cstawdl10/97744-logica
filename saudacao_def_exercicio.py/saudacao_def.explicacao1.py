import os
os.system ("clear")

def saudacao(nome):
    print(f"Olá {nome}! Bem vindo(a) ao curso de DS!")

def disciplina(nome):
    print(f"A disciplina {nome} faz parte do curso de DS.")

nome = input("Digite seu nome: ")
nome_disciplina = input("Digite o nome da disciplina: ")

saudacao(nome)
disciplina(nome_disciplina)