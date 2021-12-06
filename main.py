"""Auteurs : Team de bg's"""

# Lecure du fichier

with open("data1.dat", "r") as f:
    # Lecture du fichier
    x = []
    N = int(f.readline())
    B = int(f.readline())
    E = int(f.readline())

    for line in f:
        x.extend(line.strip().split('\t'))

x_bis = map(int, x)
x_list=list(x_bis)

print(N, B, E)
print(x_list)
