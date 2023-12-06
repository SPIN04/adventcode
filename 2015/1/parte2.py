# Apre il file in modalità lettura ('r' sta per 'read')
with open('a.txt', 'r') as file:
    # Legge il contenuto del file
    contenuto = file.read()
    piano=0
    i=0
    for a in contenuto:
        i=i+1
        if a=='(':
            piano=piano+1
        elif a==')':
            piano=piano-1
        if piano<0:
            print(i)
            break
