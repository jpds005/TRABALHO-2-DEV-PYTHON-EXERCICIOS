import os

try:
    arquivos = os.scandir()
    for obj in arquivos:
        print(obj.name)
        print(obj.path)
        print(obj.is_dir())
except FileNotFoundError:
    print("Caminho não existe")
except NotADirectoryError:
    print("O caminho ñ é diretorio")