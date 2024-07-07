
#Foi criada uma função para cada operação possível
#Cada função retorna sua respectiva operação
# Função para adição
def add(x, y):
    return x + y

# Função para subtração
def subtract(x, y):
    return x - y

# Função para multiplicação
def multiply(x, y):
    return x * y

# Função para divisão
def divide(x, y):
    if y == 0: #testa se o usuário adicionou um valor inválido
        return "Não é possível dividir por zero."
    return x / y

# Solicitação da operação ao usuário
print("Selecione a operação:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    # Recebe a escolha do usuário
    choice = input("Digite a opção (1/2/3/4): ")

    # Verifica se a escolha é válida
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Verifica se o usuário deseja fazer outra operação
        next_calculation = input("Deseja fazer outra operação? (sim/não): ")
        if next_calculation.lower() == "não":
            break
    else:
        print("Entrada inválida")
