n = int(input())

with open("rez1.txt","w") as f:
    for i in range(n):
        s = input()

        if s=="SP" or s=="PS": f.write("S\n")
        elif s=="RS" or s=="SR": f.write("R\n")
        elif s=="RP" or s=="PR": f.write("P\n")
        elif s[0]==s[1]:f.write(s[0]+"\n")

