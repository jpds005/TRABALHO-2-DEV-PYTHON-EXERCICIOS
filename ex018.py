def Divide():
    num1 = int(input("1 num: "))
    num2 = int(input("2 num: "))
    result = num1 / num2
    print(f"divisão: {result}")

def VerificarDivisao():
    try:
        Divide()
    except ValueError:
        print("Dado informado invalido")
    except ZeroDivisionError:
        print("disião por zero")


VerificarDivisao()