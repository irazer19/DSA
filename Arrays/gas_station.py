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

https://leetcode.com/problems/gas-station/description/
"""


def canCompleteCircuit(gas, cost):
    """
    Brute force:
    For every station, we will go around the full circuit once to check if we can reach it. This takes two for loops.
    Time: O(n^2) and Space: O(1)


    Optimized:
    Edge case: If the total gas that we have is less than the total required gas to reach the stations then
    we return -1 because we dont have a solution.

    We will iterate over the gas array, and keep track of the total gas we have, and the gas required to reach the next
    station. If we are short on gas, we restart (totalGas = 0) and assume the next station could be the answer.

    Time: O(n) and Space: O(1)
    """
    # Edge case, if the consumption is greater than input gas, then we return -1
    if sum(gas) < sum(cost):
        return -1
    # The total gas we currently have.
    totalGas = 0
    startStation = 0
    # For each station.
    for i in range(len(gas)):
        totalGas += gas[i]  # Recharge gas
        needed = cost[i]  # To reach the next station
        # If we are short on fuel, we restart and assume the next station could be the answer
        # therefore, totalGas = 0
        if totalGas < needed:
            startStation = i + 1
            totalGas = 0
        else:  # Else we subtract the used gas
            totalGas -= needed
    # Result
    return startStation
