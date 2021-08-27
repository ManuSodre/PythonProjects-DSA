# Implementando uma Calculadora em Python

print("\n******************* Python Calculator *******************")

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def mult(x, y):
	return x * y

def div(x, y):
    c = ( x / y ) if y != 0 else 0 # Tratamento para quando a divisão possui um denominador igual a 0
    return c

print("\nNúmero da operação: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '1':
	print("\n")
	print(num1, "+", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-", num2, "=", sub(num1, num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*", num2, "=", mult(num1, num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/", num2, "=", div(num1, num2))
	print("\n")

else:
	print("\nOpção Inválida!")
