class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq_map = Counter(hand)
        for num in sorted(freq_map):
            while freq_map[num] > 0:
                for next_num in range(num, num + groupSize):
                    if freq_map[next_num] == 0:
                        return False
                    freq_map[next_num] -= 1

        return True
