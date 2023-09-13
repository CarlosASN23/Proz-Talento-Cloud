def Menu():

    Menu =  """ \n

===== Menu de operações =====
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair 
=============================    
=>  """

    return input(Menu)

def Soma(num1,num2,res,/):

    res = num1 + num2

    print(f"\nOperação de adição realizada com sucesso, seu resultado foi: {res}")

    return Soma

def Subtracao(num1,num2,res,/):

    res = num1-num2
    print(f"\nOperação de subtração realizada com sucesso, seu resultado foi: {res}")

    return Subtracao

def Multiplicacao(num1,num2,res,/):

    res = num1*num2
    print(f"\nOperação de multiplicação realizada com sucesso, seu resultado foi: {res}")

    return Multiplicacao

def Divisao(num1,num2,res,/):

    if num2 != 0:
        res = num1/num2
        print(f"\nOperação de divisão realizada com sucesso, seu resultado foi: {res}")

    else:
        res = print("\nNão existe divisão por zero!")
    
    return Divisao

def main():

    while True:

        opcao = Menu()
        res = 0
    
        if opcao == "1":

            num1 = float(input("1º - Entre com o valor do primeiro numero: "))
            num2 = float(input("2º - Entre com o valor do segundo numero: "))

            
            res = Soma(num1,num2,res)

        elif opcao == "2":

            num1 = float(input("1º - Entre com o valor do primeiro numero: "))
            num2 = float(input("2º - Entre com o valor do segundo numero: "))

            res = Subtracao(num1,num2,res)
            

        elif opcao == "3":

            num1 = float(input("1º - Entre com o valor do primeiro numero: "))
            num2 = float(input("2º - Entre com o valor do segundo numero: "))

            res = Multiplicacao(num1,num2,res)
            

        elif opcao == "4":

            num1 = float(input("1º - Entre com o valor do primeiro numero: "))
            num2 = float(input("2º - Entre com o valor do segundo numero: "))

            res = Divisao(num1,num2,res)

        elif opcao == "0":

            print("""Obrigado por usar nossa calculadora!\nSaindo...
                  """)
            break

        else:
            print("Insira um valor válido para realizar a operação!")

main()
