# Apre il file in modalità lettura ('r' sta per 'read')
result = []

with open('a.txt', 'r') as file:
    # Legge il contenuto del file riga per riga
    for riga in file:
        dimension = riga.split('x')
        l = int(dimension[0])
        w = int(dimension[1])
        h = int(dimension[2])
        a = [l, w, h]
        a.sort()
        min_area = (a[0] + a[1])*2
        risultato = l*w*h+ min_area
        result.append(risultato)

print(sum(result))
