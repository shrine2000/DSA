class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime_numbers = self.sieve(n)
        ans = []
        
        i, j = 0, len(prime_numbers) - 1
        
        while i <= j:
            if prime_numbers[i] + prime_numbers[j] == n:
                ans.append([prime_numbers[i], prime_numbers[j]])
                i += 1
                j -= 1
            elif prime_numbers[i] + prime_numbers[j] < n:
                i += 1
            else:
                j -= 1
        
        return ans

    def sieve(self, n):
            prime = [True for i in range(n+1)]
            p = 2
            arr=[]
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            for p in range(2, n+1):
                if prime[p]:
                    arr.append(p)
            return arr