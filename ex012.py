import math
num = -2

try:
    result = math.sqrt(num)
    print("A raiz quadrada", result)
except Exception:
    print("não existe a raiz quadrada de numero negativo")