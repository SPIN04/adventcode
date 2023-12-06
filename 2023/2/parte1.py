scartato = []


def check(colore, valore, id):
  if colore == 'red':
    if valore > 12:
      scartato.append(id)
  if colore == 'green':
    if valore > 13:
      scartato.append(id)
  if colore == 'blue':
    if valore > 14:
      scartato.append(id)


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
  estrazione_counter = 1  # Contatore per numerare le estrazioni
  while riga:
    output = step(riga)

    # Verifica se la lista output non è vuota
    if output:
      try:
        estrazione_counter = 1
        print(f"\n\n\nGame {output['id']}:")
        for estrazione in output['estrazioni']:
          print(f"\n\nEstrazione {estrazione_counter}")
          for elemento in associativo([estrazione]):
            for colore in elemento:
              colore_nome = list(colore.keys())[0]
              valore = colore[colore_nome]
              print(f"{colore_nome}: {valore}")
              check(colore_nome, valore, output['id'])
          estrazione_counter += 1
      except Exception as e:
        ciao = 0

    riga = file.readline()

numbers_array = [str(i) for i in range(1, 101)]
#print(numbers_array)
scartato = list(set(scartato))
#print(scartato)

filtered_numbers = [num for num in numbers_array if num not in scartato]
sommaIndici = somma(filtered_numbers)
print(f"\n\n\nSomma indici: {sommaIndici}")
# Print the result
#print("filtro")
#print(filtered_numbers)
print('')
print('')
print('')
print(
    "fine output file-------------------------------------------------------------"
)
