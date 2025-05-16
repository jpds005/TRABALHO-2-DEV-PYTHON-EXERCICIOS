import os

try:
    os.rename("teste_orig.txt", "teste_desk.txt")
    print("Arquivo renomiado")
except FileNotFoundError as erro:
    print(f"erro {erro}")
    print("Aviso: arquivo inexistente")
except PermissionError as erro:
    print(f"erro: {erro}")
    print("Aviso sem permição de acesso")
except FileExistsError as erro:
    print(f"Erro: {erro}")
    print("aQUIVO DESTINO ja existe")