from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        simulation,
        1. start from all idx


        """

        N = len(gas)
        for station, index in enumerate(gas):
            _tank = 0
            for i in range(N):
                circular_idx = (station + i) % N
                _tank += gas[circular_idx]
                if _tank < cost[circular_idx]:
                    break
                _tank -= cost[circular_idx]
            else:
                return station
        return -1


if __name__ == "__main__":
    pass
