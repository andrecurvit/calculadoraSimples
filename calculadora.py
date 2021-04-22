# -*- coding: utf-8 -*-

#Criado por: Andre Almeida
#Data: 22/04/2021


print("--------CACLCULADORA v1.0-----------")
print("------= by: Andre Almeida ----------")
print("---------- BEM VINDO!!! ------------")

sair = False
while sair == False:


    n1 = input('Insira o primeiro número: ') #Recolhe o primeiro número
    n1 = int(n1) #define o tipo de dado da variável 1
    op = input("Insira o operador (+ - * /): ") # escolha o operador para fazer o cálculo
    n2 = input("Insira o segundo número: ") #recolhe o segundo valor
    n2 = int(n2) #define o tipo de dado da variável 2

    print ("================Calculando...=================")
    print ("==================Pronto!=====================")
    # + soma
    if op  == "+":
        op = n1 + n2
    # - subtração
    if op == "-":
        op = n1 - n2
    # * multiplicação
    if op == "*":
        op = n1 * n2
    # / divisão
    if op == "/":
        op = n1 / n2

    print("Resultado")
    print(op)
    teste = input("Deseja sair? (n/s): ")
    if teste == "s" or "S":
        sair = True
