import os 

try:
    os.remove("teste.txt")
    print("Arquivo removido")
except FileNotFoundError as erro:
    print(f"erro {erro}")
    print("Aviso: arquivo inexistente")
except PermissionError as erro:
    print(f"erro: {erro}")
    print("Aviso sem permição de acesso")
except IsADirectoryError as erro:
    print(f"Erro: {erro}")
    print("Tentativa de remover diretorio")