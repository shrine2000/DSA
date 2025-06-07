class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus, current_surplus = 0, 0
        idx = 0

        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            total_surplus += delta
            current_surplus += delta

            if current_surplus < 0:
                current_surplus = 0
                idx = i + 1
        return idx if total_surplus >= 0 else -1
