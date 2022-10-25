"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""


def canCompleteCircuit(gas, cost):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    Edge case: If the total gas that we have is less than the total required gas to reach the stations then
    we return -1 because we dont have a solution.
    At each station, we will compute the difference,
    gas left = current gas - gas which will be consumed for next station.
    If the sum of total left gas + diff is -ve, then we know that we cannot each the next station, so
    whatever starting index we had earlier is invalid, and thus we reset total gas left = 0, and update the
    potential starting index as the next station.

    Else, if the sum of total left gas + diff > 0, then we know that we can still reach the next station,
    So we keep moving.

    Idea: The first station using which we can reach the end of the array without the gas going -ve is the correct
    starting station.
    """
    # Edge case, if the consumption is greater than input gas, then we return -1
    if sum(gas) < sum(cost):
        return -1
    # This variable will track the total gas left from the previous station, as we move forward from a
    # starting station.
    totalGas = 0
    # Result
    startStation = 0
    # For each station.
    for i in range(len(gas)):
        # We will compute the difference between input gas - consumed gas.
        diff = gas[i] - cost[i]
        # If the sum of previous total gas + diff > 0
        if totalGas + diff < 0:
            # We reset the total gas to 0 because the previous starting station is invalid as we cannot reach
            # the next station.
            totalGas = 0
            # We make the potential starting station = next station.
            startStation = i + 1
        else:
            # Else, if the sum above is position then we can definitely reach the next station, so we add
            # the left over gas to the current total gas.
            totalGas += diff

    # Result
    return startStation
