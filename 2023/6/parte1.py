# Apre il file in modalità lettura
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
    print(time,'\n',record)
    for i, val in enumerate(time):
        tmz=0
        tempodisposizione=int(val)
        while tmz*tempodisposizione<=int(record[i]):
            tmz+=1
            tempodisposizione-=1
        print(tmz,tempodisposizione,tmz*tempodisposizione)
