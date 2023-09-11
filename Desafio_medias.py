# Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. 
# Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

def calculadora(num1,num2,numOpe):

    # Bloco para a execução da operação de adição
    if numOpe == 1:
        res= num1+num2

    # Bloco para a execução da operação de subtração
    elif numOpe == 2:
        res = num1 - num2

    # Bloco para a execução da operação de multiplicação
    elif numOpe == 3:
        res = num1*num2

    # Bloco para a execução da operação de divisão
    elif numOpe == 4:
        
        # Bloco If para verificação de num2 igual a zero (não existe divisão por zero)
        if num2 ==0:
            res= print("Não existe divisão por zero")
        # Bloco para a validação e execução em caso de num2 diferente de 0
        elif num2 !=0:
            res = num1/num2

    # Bloco Else para conferência de valor informado diferente dos parametros de 1 a 4 p/ as operações
    else:
        res=0

    return res

# Impressão dos resultados
resultado =calculadora(5,2,5)
print(resultado)