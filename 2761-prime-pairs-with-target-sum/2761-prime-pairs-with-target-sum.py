class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime_numbers = self.generate_primes(n)
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

    def generate_primes(self, n):
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False

        for p in range(int(n**0.5) + 1, n + 1):
            if sieve[p]:
                primes.append(p)

        return primes
