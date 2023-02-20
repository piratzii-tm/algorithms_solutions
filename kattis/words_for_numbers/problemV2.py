#codul pus pe kattis

import fileinput

numbersDict = {
    0:"zero",
    1:"one", 11:"eleven", 30:"thirty",
    2:"two", 12:"twelve", 40:"forty",
    3:"three", 13:"thirteen", 50:"fifty",
    4:"four", 14:"fourteen",60:"sixty",
    5:"five", 15:"fifteen", 70:"seventy",
    6:"six", 16:"sixteen", 80:"eighty",
    7:"seven", 17:"seventeen", 90:"ninety",
    8:"eight", 18:"eighteen",
    9:"nine", 19:"nineteen",
    10:"ten", 20:"twenty",
}

def transform(number):
    decomp = []
    p = 1
    while number:
        decomp.append(number%10 * p)
        p*=10
        number//=10
    decomp.sort(reverse=True)
    res = ""
    s = sum(i for i in decomp) 
    if s not in numbersDict:
        for i in decomp:
            i = numbersDict[i]
            res += i+"-"
        res = res[:-1]
    else:res=numbersDict[s]
    return res




resL = []
res = ""
for prop in fileinput.input():
    prop = prop.split(" ")
    prop[len(prop)-1] = prop[len(prop)-1][:-1]
    for word in range(len(prop)):
        try:
            digit = int(prop[word])
            digit = transform(int(prop[word]))
            if word == 0:
                aux = chr(ord(digit[0])-32)
                aux += digit[1:]
                digit = aux
            prop[word] = digit
        except: continue
    for i in prop:
        res+=i+" "

    res = res[:-1]
    resL.append(res)
    res = ""
    
for i in resL:
    print(i)