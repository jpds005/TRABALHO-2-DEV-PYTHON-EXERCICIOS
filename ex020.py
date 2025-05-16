try:
    print("Abrndo um arquivo")
    open("texto.txt", "r")
except FileNotFoundError as captura:
    print(captura)