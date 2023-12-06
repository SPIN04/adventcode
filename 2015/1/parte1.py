# Apre il file in modalità lettura ('r' sta per 'read')
with open('a.txt', 'r') as file:
    # Legge il contenuto del file
    contenuto = file.read()
    a=contenuto.count('(')
    b=contenuto.count(')')
    print(a-b)
