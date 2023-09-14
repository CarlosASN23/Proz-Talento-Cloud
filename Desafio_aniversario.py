# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def aniversario():

    nome = input("Entre com o seu nome completo: ")

    while True:

        try:

            nascimento = int(input("Entre com o ano de seu nascimento: "))

            if nascimento < 1922 or nascimento > 2021:
                print("Entre com um ano entre 1922 e 2021")
                
            elif nascimento >= 1922 and nascimento<=2021:

                idade = 2022 - nascimento
                print(f"{nome} nasceu no ano de {nascimento} e completou/completará {idade} anos em 2022")
                break

        except:
            print("Entre com um número válido")
           
aniversario()