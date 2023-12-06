grattini = []
grattini2 = []

with open('a.txt', 'r') as file:
    for line in file:
        line = line.replace('Card ', '').replace('\n', '')
        grattini.append(line.split(':')[1].split(" | "))
        grattini2.append(line.split(':')[1].split(" | "))


for i, gratta in enumerate(grattini):
    vincenti = set(int(numero) for numero in gratta[0].split(' ') if numero.isdigit())
    miei = set(int(numero) for numero in gratta[1].split(' ') if numero.isdigit())

    numeri_in_comune = vincenti & miei
    copie = len(numeri_in_comune)

    if copie > 0:
        array = []
        for x in range(copie):
            array.append(str(i+(x+1)))
            print("aaaaaaa     ",i+x)
        print(array)
        grattini2.append(array)

print(len(grattini2))
