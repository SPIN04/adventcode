import time
import math
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
    print(array_attuale)
    time.sleep(5)
    
    
    r = []
    print("start while")
    for i in range(len(array_attuale)):
        x = 0
        pippo = True
        while pippo:
            print(f"while: {x}")    
            print(f"\t\t\t\tfor: {i}")
            array_attuale[i] = pluto(array_attuale[i], istruzioni[x % len(istruzioni)])
            x+=1
            if (array_attuale[i].endswith("Z")):
                pippo = False
                r.append(x)           
    print(r)


