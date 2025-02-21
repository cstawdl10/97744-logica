import os
os.system("clear")


print("""
======================= MENU =======================
Código          \tPrato                \tValor
1               \tPicanha              \t:130,00
2               \tPizza grande         \t:55,00
3               \tPizza média          \t:40,00
4               \tPizza pequena        \t:25,00
""")

print()
opcoes = int(input("Digite o código do prato desejado: "))

match opcoes:
    case 1:
         opcoes = ("Picanha valor: 130,00")
    case 2:
          opcoes = ("Pizza Grande valor: 55,00")
    case 3:
          opcoes = ("Pizza Média valor: 40,00")
    case 4:
         opcoes = ("Pizza Pequena valor: 25,00")




print(f" {opcoes}")

