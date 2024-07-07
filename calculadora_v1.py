# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Selecione o número da operação desejada:","\n")
print(" 1 - Adição","\n","2 - Subtração","\n","3 - Multiplicação","\n","4 - Divisão","\n")

operacao = input("Digite a operação desejada (1/2/3/4):")

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

if (operacao=="1"):
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)
elif operacao == "2":
    resultado = numero1 - numero2
    print("O resultado da subtração é: ", resultado)
elif operacao == "3":
    resultado = numero1 * numero2
    print("O resultado é: ", resultado)
elif operacao == "4":
    resultado = numero1 / numero2
    print("O resultado é: ", resultado)
else:
    print("Escolha uma operação válida!")



