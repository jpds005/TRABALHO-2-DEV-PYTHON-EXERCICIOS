def ReadFile():
    try:
        print("Abrndo um arquivo")
        open("texto.txt", "r")
    except FileNotFoundError:
        print("O arquivo não existe")
    

    ReadFile()