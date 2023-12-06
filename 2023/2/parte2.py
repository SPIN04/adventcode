tmp_r = []
tmp_g = []
tmp_b = []
smx=[]
idd='1'
def check(colore, valore, id):
    global idd, tmp_r, tmp_g, tmp_b,somma
    #id=str(int(id)-1)
    if id == idd:
        if colore == 'red':
            tmp_r.append(valore)
        elif colore == 'green':
            tmp_g.append(valore)
        elif colore == 'blue':
            tmp_b.append(valore)
    else:
        # If the id changes, reset the lists
        idd = id

        r = max(tmp_r)
        g = max(tmp_g)
        b = max(tmp_b)
        print(r,g,b)
        tmp_r = []
        tmp_g = []
        tmp_b = []

        ex=r*g*b
        smx.append(ex)
        if colore == 'red':
            tmp_r.append(valore)
        elif colore == 'green':
            tmp_g.append(valore)
        elif colore == 'blue':
            tmp_b.append(valore)


def step(riga):
  riga = riga.replace('Game ', '').replace(', ',
                                           ',').replace('; ', ';').replace(
                                               ': ', ':').replace(' ', '%')

  id_val = getid(riga)
  rpl = id_val + ':'
  riga = riga.replace(rpl, '')

  giocate = game(riga)
  estrazioni = [get_estrazione(g) for g in giocate]

  return {'id': id_val, 'estrazioni': estrazioni}


def getid(riga):
  return riga.split(':')[0]


def game(riga):
  return riga.replace('\n', '').split(';')


def get_estrazione(giocata):
  return giocata.split(',')


def associativo(extra):
  assoc = []
  for estrazione in extra:
    tmp = []
    for colore in estrazione:
      tmp.append({getvar(colore): getnum(colore)})
    assoc.append(tmp)
  return assoc


def getnum(s):
  return int(s.split('%')[0]) if s.split('%')[0].isdigit() else 0


def getvar(s):
  return s.split('%')[1].replace('\n', '')


def somma(array):
  somma = 0
  for i in range(len(array)):
    n = int(array[i])
    if n != 0:
      somma += n
  return somma

print(
    "inizio output file-------------------------------------------------------------"
)
print('')
print('')
print('')

with open('a.txt', 'r') as file:
    riga = file.readline()
    estrazione_counter = 1

    while riga:
        output = step(riga)

        if output:
            try:
                estrazione_counter = 1
                #print(f"\n\n\nGame {int(output['id'])-1}:")
                for estrazione in output['estrazioni']:
                    #print(f"\n\nEstrazione {estrazione_counter}")
                    for elemento in associativo([estrazione]):
                        for colore in elemento:
                            colore_nome = list(colore.keys())[0]
                            valore = colore[colore_nome]
                            #print(f"game:{output['id']} ____{colore_nome}: {valore}")
                            check(colore_nome, valore, output['id'])
                    estrazione_counter += 1
            except Exception as e:
                print(e)

        riga = file.readline()
print(sum(smx))
print('')
print('')
print('')
print("fine output file-------------------------------------------------------------")

