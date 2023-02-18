files = ["00-example.txt","01-the-cloud-abyss.txt","02-iot-island-of-terror.txt","03-etheryum.txt","04-the-desert-of-autonomous-machines.txt","05-androids-armageddon.txt"]

numberOfResponse = 0
for fileName in files:


    with open("response{}.txt".format(numberOfResponse),"w") as y:

        sc = []
        tr = []
        sr = []


        defeated = []

        with open(fileName,"r") as f:
            r = f.readline().split(" ")
            si,smax,t,d = int(r[0]),int(r[1]),int(r[2]),int(r[3])
            for i in range(d):
                r = f.readline().split(" ")
                
                sc.append(int(r[0])) #sc
                tr.append(int(r[1])) #tr
                sr.append(int(r[2])) #sr
                ni = int(r[3])



        def search(sr,sc,defeated,si):
            response = -1
            max = -1
            for i in range(d):
                if sr[i] > max and sc[i] <= si and i not in defeated:
                    max = sr[i]
                    response = i
            
            return response

        k = []

        rez = []

        for i in range(t):
            aux = []
            for j in range(len(k)):
                if k[j][0] == i:
                    si += k[j][1]
                else: aux.append(k[j])
            k = aux

            demon = search(sr,sc,defeated,si)
            if demon != -1:
                y.write(str(str(demon)+"\n"))
                defeated.append(demon)
                si -= sc[demon]
                k.append([i+tr[demon],sr[demon]])

        for i in range(d):
            if i not in defeated:
                defeated.append(i)
                y.write(str(str(i)+"\n"))

        
                
        numberOfResponse+=1