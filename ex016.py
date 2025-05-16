def dividir(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is", result)

dividir(2, 2)
dividir(0, 0)