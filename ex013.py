import math
num = -2

try:
    result = math.sqrt(num)
    print("A raiz quadrada", result)
except ValueError:
    print("não existe a raiz quadrada de numero negativo")
    num = -num
    print("transformando o numero em positivo")
    result = math.sqrt(num)
    print(f'A raiz quadrada é {result}')