def aseazaUndeTrebuie(lista, elemntul):
    i = 0 
    
    while i<len(lista) and lista[i][0] >= elemntul[0]:
        i+=1
    
    lista.append("random")

    j = len(lista) - 1
    while j > i:
        lista[j] = lista[j-1]
        j-=1

    lista[i] = elemntul

    return lista

#procesare input
with open("00-example.txt", "r") as f:

    first = f.readline().split(" ")
    coloana = int(first[0])
    linie = int(first[1])
    nrSerpi = int(first[2])

    lungimiSerpi = f.readline().split(" ")
    lungimiSerpi = [int(i) for i in lungimiSerpi]

    pozitiiDisponibile = []
    mapa = []
    
    for i in range(linie):
        tempRand = f.readline().split()
        tempRand2 = []
         
        for j in range(len(tempRand)):
            tempValue = tempRand[j]
            if tempValue != "*":
                tempValue = int(tempValue)
                tempRand2.append(tempValue)
                if not len(pozitiiDisponibile): pozitiiDisponibile.append([tempValue,i,j])
                else: 
                    if type(tempValue) != "String":
                        pozitiiDisponibile=aseazaUndeTrebuie(pozitiiDisponibile,[tempValue,i,j])
            else: 
                tempRand2.append(tempRand[j])
        
        mapa.append(tempRand2)

    print(coloana,"\n",linie,"\n",nrSerpi,"\n",lungimiSerpi,"\n",pozitiiDisponibile,"\n")
    for i in mapa: print(i,"\n")

     

        


