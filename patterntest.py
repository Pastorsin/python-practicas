from pattern.es import parse, split

frase = "Hoy es un muy lindo dia"
s = parse(frase).split()
print(s)

for cada in s:
    for c in cada:
        if c[1] == 'VB':
            print(c[0])
