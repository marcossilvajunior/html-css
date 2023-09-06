
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
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Mostra o menu da calculadora
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita a escolha do usuário
choice = input("Digite a opção (1/2/3/4): ")

# Verifica a escolha do usuário
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == '1':
        print("Resultado:", add(num1, num2))
    elif choice == '2':
        print("Resultado:", subtract(num1, num2))
    elif choice == '3':
        print("Resultado:", multiply(num1, num2))
    elif choice == '4':
        print("Resultado:", divide(num1, num2))
else:
    print("Opção inválida")
