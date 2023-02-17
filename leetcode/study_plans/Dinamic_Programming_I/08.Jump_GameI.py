class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        indexList = [0 for i in range(n)]

        indexList[0] = nums[0]
        if n == 1 and nums[0]>=0: return True # daca lista de numere are un singur element si elementul respectiv nu este negativ returnam TRUE
        elif indexList[0] == 0: return False #daca lista are mai multe elemente si primul element este 0 inseamna ca nu poate continua deci returnam FALSE
        elif indexList[0] == n-1: return True #daca primul element din lista indica spre ultimul se face o singura saritura deci indicam TRUE

        k=0

        for i in range(1,n):
            accesibil = False

		#aici verificam daca elementul pe care ne aflam este accesibil, adica daca este vreun numar inaintea sa de pe care putem ajunge aici
		#verificarea incepe de pe un anume element k deoarece k reprezinta elementul cu cea mai mare saritura la momentul respectiv
            for j in range(k,i):
                if indexList[j]>=i: 
                    k=j
                    accesibil = True
                    break
            #daca elementul este accesibill atunci ii putem atribui valoare
            if accesibil: 
                indexList[i] = i + nums[i]
                if indexList[i] == n-1: return True
            else: return False #daca elementul nu este accesbil inseamna ca nu exista inaintea sa niciun element care sa indice spre nici o valoare mai mare sau egala cu acesta, deci prin urmare nu exista niciun element care sa indice spre ultimul element al liste de numere

        return True
            



