#Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
#Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

Andar = 20
i = 0

# Sem laços de repetição em ordem crescente
print("Sem utilizar laços de repetição")
print(f"Andar nº {i+1}")
print(f"Andar nº {i+2}")
print(f"Andar nº {i+3}")
print(f"Andar nº {i+4}")
print(f"Andar nº {i+5}")
print(f"Andar nº {i+6}")
print(f"Andar nº {i+7}")
print(f"Andar nº {i+8}")
print(f"Andar nº {i+9}")
print(f"Andar nº {i+10}")
print(f"Andar nº {i+11}")
print(f"Andar nº {i+12}")
print(f"Andar nº {i+14}")
print(f"Andar nº {i+15}")
print(f"Andar nº {i+16}")
print(f"Andar nº {i+17}")
print(f"Andar nº {i+18}")
print(f"Andar nº {i+19}")
print(f"Andar nº {i+20}")

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


