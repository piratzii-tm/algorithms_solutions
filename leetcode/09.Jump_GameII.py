class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        listIndex = [i + nums[i] for i in range(n)] #creem lista cu indexi, adica spre ce element arata fiecare dintre ele


        k = n-1
        h = 0

        while k!=0:
	#pornind de pe elementul k cautam in intervalul [0,k-1] cel mai mic index i pentru care valoare spre care arata acesta este mai mare sau egala cu elementul k
	# spre exemplu in lista indexList=[2,4,3,4,8] k=4 si cel mai mic i cu indexList[i]>=k este 1 si tot asa pana ajungem la 0
            min = k
            for i in range(k):
                if listIndex[i]>=k and min>i:
                    min = i
            k = min
	#de fiecare data cand ii atribuim o valoare lui k crestem o variabila h cu un, aceasta variabila reprezentand numarul de sarituri(practic noi sarim inapoi :)) )
            h+=1
        return h
            
