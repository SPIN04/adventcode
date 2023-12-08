matrice = {}

with open("2023/8/a.txt", "r") as file:
    istruzioni = file.readline().strip()

    for line in file:
        line = line.strip().replace(" ", "").replace("(", "").replace(")", "")
        riga = line.split("=")
        nodoCorrente = riga[0]
        dest = riga[1].split(",")
        left = dest[0]
        right = dest[1]
        matrice[nodoCorrente] = (left, right)

i = 0
attuale = "AAA"

while attuale != "ZZZ":
    print(f"next iteration: {i}")

    if istruzioni[i % len(istruzioni)] == "L":
        attuale = matrice[attuale][0]
        print("sinistra")
    else:
        attuale = matrice[attuale][1]
        print("destra")

    i += 1
    print(attuale)

print(f"Step: {i}")