
flag=0
def has_no_duplicates_except_spaces(string):
    # Rimuovi gli spazi dalla stringa
    string_without_spaces = string.replace(" ", "")
    
    # Crea un set dei caratteri della stringa senza spazi
    unique_chars = set(string_without_spaces)
    
    # Se la lunghezza del set è uguale alla lunghezza della stringa senza spazi,
    # significa che non ci sono duplicati.
    if len(unique_chars) == len(string_without_spaces):
        return True  # Non ci sono duplicati
    else:
        return False  # Ci sono duplicati
    
with open("2024/2/input.txt", "r") as file:
    arr_diff=[]
    for line in file:
        # Divide la riga in parole, ordina le parole, poi riuniscile con uno spazio
        current = " ".join(sorted(line.split()))
        if (current==line.strip() or current[::-1]==line.strip() and has_no_duplicates_except_spaces(line) ):
            

            
            
            
            arr_current=current.split(" ")
            local=[]
            for num1, num2 in zip(arr_current, arr_current[1:]):
                local=[]
                diff=abs(int(num1)-int(num2))
                local.append(diff)
            arr_diff.append(local)
            
    print(arr_diff)
