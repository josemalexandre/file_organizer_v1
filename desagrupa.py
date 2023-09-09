import os

pastas = []

for i in os.listdir():
    if os.path.isdir(i):
        pastas.append(i)

for i in pastas:
    for j in os.listdir(i):
        os.rename(f'{os.getcwd()}\{i}\{j}', f'{os.getcwd()}\{j}')
    os.rmdir(i)
