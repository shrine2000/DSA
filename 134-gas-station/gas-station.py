class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        total_tank = 0
        curr_tank = 0
        start_idx = 0

        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            curr_tank += net_gain
            total_tank += net_gain

            if curr_tank < 0:
                start_idx = i + 1
                curr_tank = 0

        return start_idx if total_tank >= 0 else - 1