def Divide():
    try:
        num1 = int(input("1 num: "))
        num2 = int(input("2 num: "))
        result = num1 / num2
        print(f"divisão: {result}")
    except ValueError:
        print("dado informado invalido")
    except ZeroDivisionError:
        print("Divisão por zero!")

Divide()