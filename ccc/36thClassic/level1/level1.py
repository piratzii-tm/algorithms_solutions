n = int(input())
m = []
k=0
for i in range(n):
    s= input()
    for j in s:
        if j == 'C':
            k+=1
print(k)