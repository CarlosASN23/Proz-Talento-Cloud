#Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
#Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

Andar = 20
i = 0

# Utilizando laço For com decrimento dentro da função
for i in range(20,0,-1):

    if i == 13:
        continue
    else:
        print(f"Andar nº {i}")

print("\n")

# Utilizando o laço de repetição While e imprimindo em ordem decrescente
print("Utilizando laços de repetição While")
while (Andar > i):

    result = Andar - i
    i +=1
    if result == 13:
        continue
    print(f"Andar nº {result}")

print("\n")

# Utilizando o laço de repetição For em ordem decrescente
print("Utilizando laço de repetição For")
for i in range(Andar):

    result = Andar - i

    if result == 13:
        continue
    print(f"Andar nº {result}")


