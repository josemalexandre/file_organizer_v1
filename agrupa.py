import os

camiho = os.getcwd()

diretorios_arquivos = []

for i in os.listdir():
    if os.path.isfile(i):
        diretorios_arquivos.append(f'{camiho}\{i}')

extensoes = set()

for i in diretorios_arquivos:
    if os.path.splitext(i)[1].replace('.', '').upper() != 'PY':
        extensoes.add(os.path.splitext(i)[1].replace('.', '').upper())

for i in extensoes:
    os.mkdir(f'{i}')

for i in diretorios_arquivos:
    for j in extensoes:
        if os.path.splitext(i)[1].replace('.', '').upper() == j:
            os.rename(i, f'{camiho}\{j}\{os.path.split(i)[1]}')
