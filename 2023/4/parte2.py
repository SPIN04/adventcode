matrice = []
grattini =[]
somma = 0

with open('2023/4/a.txt', 'r') as file:
    for line in file:
        line = line.strip().replace('Card ', '').replace('\n', '').replace("' ", "'")
        grattini.append(line.split(':')[1].split(" | "))

        numero_prima_dei_due_punti = line.split(':', 1)[0]
        matrice.append([numero_prima_dei_due_punti, 1])

    

for i, gratta in enumerate(grattini):
    vincenti = gratta[0].split(' ')
    miei = gratta[1].split(' ')
    # Stampa la matrice
    for riga in matrice:
        print(riga)
    print("\n\n", matrice[0][0], i)
    numvinc = set(int(numero) for numero in vincenti if numero.isdigit())
    munmiei = set(int(numero) for numero in miei if numero.isdigit())

    numeri_in_comune = numvinc & munmiei
    copie = len(numeri_in_comune)

    for x in range(copie):
        matrice[i+x+1][1]+=(1*matrice[i][1])
    # Stampa la matrice

    for riga in matrice:
        print(riga)
    print("\n\n----------------------------------------------------------------------------------")
    


somma = 0
for riga in matrice:
    try:
        numero_da_sommare = int(riga[1])
        somma += numero_da_sommare
    except (ValueError, IndexError):
        # Gestisci eventuali errori se il valore non è un intero o se la colonna non esiste
        pass
print(somma)  
    