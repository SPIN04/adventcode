matrice = {}
array_attuale = []

def pluto(idAttuale, istruzione):
    if istruzione == "L":
        return matrice[idAttuale][1]
    else:
        return matrice[idAttuale][2]

with open("2023/8/a.txt", "r") as file:
    istruzioni = file.readline().strip()

    for i, line in enumerate(file):
        line = line.strip().replace(" ", "").replace("(", "").replace(")", "")
        riga = line.split("=")
        nodoCorrente = riga[0]

        if nodoCorrente.endswith("A"):
            array_attuale.append(nodoCorrente)

        dest = riga[1].split(",")
        left = dest[0]
        right = dest[1]
        matrice[nodoCorrente] = (nodoCorrente, left, right)

        #for i in matrice:
            #print(matrice[i])

    pippo = True
    x = 0
    print("start while")
    while pippo:
        print(f"while: {x}")
        for i in range(len(array_attuale)):
            print(f"\t\t\t\tfor: {i}")
            array_attuale[i] = pluto(array_attuale[i], istruzioni[x % len(istruzioni)])
            if  (array_attuale[i].endswith("Z")):
                pippo = False
        x+=1
    print("end while")
    print(x)
