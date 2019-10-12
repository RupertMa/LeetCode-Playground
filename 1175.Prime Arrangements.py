class Solution:
    def numPrimeArrangements(self, n: int) -> int:    
        import math
        primes = 0
        for i in range(2,n+1):
            cond = True
            for j in range(2,i):
                if i % j == 0:
                    cond = False
                    break
            if cond:
                primes += 1
        return (math.factorial(primes) * math.factorial(n-primes)) % (10**9+7)
        