import os

diretorios_arquivos = []

for i in os.listdir():
    diretorios_arquivos.append(f'{os.getcwd()}\{i}')

extensoes = set()

for i in diretorios_arquivos:
    if os.path.splitext(i)[1].replace('.', '').upper() != 'PY':
        extensoes.add(os.path.splitext(i)[1].replace('.', '').upper())
    else:
        continue

for i in extensoes:
    os.mkdir(f'{i}')

for i in diretorios_arquivos:
    for j in extensoes:
        if os.path.splitext(i)[1].replace('.', '').upper() == j:
            os.rename(i, f'{os.getcwd()}\{j}\{os.path.split(i)[1]}')
