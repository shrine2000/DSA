class Solution:
    def nthUglyNumber(self, n: int) -> int:
        un = [1]
        f = [2, 3, 5]
        pq = [1]

        while n > 1:
            su = heapq.heappop(pq)
            n -= 1
            for _f in f:
                nu = su * _f
                if nu not in un:
                    un.append(nu)
                    heapq.heappush(pq, nu)

        return pq[0]
