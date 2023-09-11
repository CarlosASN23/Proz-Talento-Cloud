def calculadora(num1,num2,numOpe):
    if numOpe == 1:
        res= num1+num2

    elif numOpe == 2:
        res = num1 - num2
    
    elif numOpe == 3:
        res = num1*num2

    elif numOpe == 4:
        if num2 ==0:
            res= print("Não existe divisão por zero")

        elif num2 !=0:
            res = num1/num2
    else:
        res=0
        
    return res

resultado =calculadora(5,2,5)
print(resultado)