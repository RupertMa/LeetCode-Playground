class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cum_sum = start = 0
        for i in range(len(gas)):
            cum_sum += (gas[i] - cost[i])
            if cum_sum < 0:
                cum_sum = 0
                start = i + 1
        return start if sum(gas) >= sum(cost) else -1
    # Time complexity: O(N)
