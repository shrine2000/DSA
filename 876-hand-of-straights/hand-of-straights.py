class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if card_count[i] == 0:
                    return False
                card_count[i] -= 1
                if card_count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
