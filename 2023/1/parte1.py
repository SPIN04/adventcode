def remove_letters(input_string, letters_to_remove):
    return ''.join(char for char in input_string if char not in letters_to_remove)

alfabeto="abcdefghijklmnopqrstuvwxyz"
c=0
with open('a.txt', 'r') as file:
    line = file.readline()
    while line:
        linea=remove_letters(line,alfabeto)
        linea=linea.replace('\n', '')
        if len(linea)==1:
          #print(int(linea)*11)
          c=c+int(linea)*11
        else:
          a=int(linea[0])*10
          b=int(linea[len(linea)-1])
          c=c+a+b
        line = file.readline()
print(c)
