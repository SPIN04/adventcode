# il file di input è lo stesso tenere gli spazi tra i : e i dati
new=[]
time=[]
record=[]
with open('2023/6/a.txt', 'r') as file:
    # Itera attraverso le linee del file
    for linea in file:
        # Stampa o esegui altre operazioni con la linea
        linea=linea.replace('Time:        ','').replace('Distance:   ','').replace('\n','')
        linea=linea.split(' ')
        for cella in linea:
            if cella!='':
                new.append(cella)
    #print(new)
    for i, cella in enumerate(new):
        if i<len(new)/2:
            time.append(cella)
        else:
            record.append(cella)
    for i, val in enumerate(time):
        count=0
        tmz=0
        tempodisposizione=int(val)
        tmxclone=0
        tempodisposizioneclone=0
        while tmz*tempodisposizione<=int(record[i]):
            tmz+=1
            tempodisposizione-=1
            tmxclone=tmz
            tempodisposizioneclone=tempodisposizione
            while tmxclone*tempodisposizioneclone>int(record[i]):
                tmxclone+=1
                tempodisposizioneclone-=1
                count+=1
            
        print(count,i)
