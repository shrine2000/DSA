class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        while hand:
            start = hand[0]
            for card in range(start, start + groupSize):
                if card not in hand:
                    return False
                hand.remove(card)
        return True