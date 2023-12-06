grattini = []
somma=0
with open('a.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace('Card ', '').replace('\n', '')
        grattini.append(line.split(':')[1].split(" | "))

for gratta in grattini:
    vincenti = gratta[0].split(' ')
    miei = gratta[1].split(' ')

    numvinc = set(int(numero) for numero in vincenti if numero.isdigit())
    munmiei = set(int(numero) for numero in miei if numero.isdigit())

    numeri_in_comune = numvinc & munmiei
    if pow(2,len(numeri_in_comune)-1)>=1:
        somma+=pow(2,len(numeri_in_comune)-1)
print(somma)
