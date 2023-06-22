class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = 'null'
        totalProfit = 0

        for price in prices:
            if buy == 'null':
                buy = totalProfit - price
            else: buy = max(buy, totalProfit - price) # maximul dintre cat am cumparat deja si cat am cumpara daca am incepe o tranzacitie in ziua respectiva

            totalProfit = max(totalProfit , buy + price - fee)
            # maximul dintre profitul pe care il avem acum si profitul pe care l-am putea avea daca incheiem tranzactia

        return totalProfit