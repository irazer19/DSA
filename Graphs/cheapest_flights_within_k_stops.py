from typing import List

"""
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


def findCheapestPrice(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    # Time: O(n + v) and Space: O(n + v)
    """
    Logic:
    To find the cheapest price from source to destination, we will use BFS starting from the source node,
    We will maintain a list of all the prices for all the cities and update it inside BFS.
    For all the next cities, we will check whether the current price to reach it is less than the existing price,
    if yes then we will update the price and append to the queue.
    """
    # Creating the graph for getting all the child cities starting from the source city
    graph = {}
    # We will also store the prices
    prices = {}
    for start, end, price in flights:
        prices[(start, end)] = price
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    # BFS
    # We will store current city, remaining stops, current price in the queue
    q = [[src, k, 0]]
    # List to store all the updated price to reach the city
    result = [float("inf") for _ in range(n)]
    # The price to reach the start city is 0
    result[src] = 0

    while q:
        currStop, remainingStops, price = q.pop(0)
        # IF we dont have any more stops left to travel then we will continue to the next city
        if remainingStops < 0:
            continue
        # For every next city from the current city
        for nextStop in graph.get(currStop, []):
            # Price to reach this next city from the current city
            priceToReachNext = price + prices[(currStop, nextStop)]
            # If the price to reach is less than the existing price, we update
            if result[nextStop] > priceToReachNext:
                result[nextStop] = priceToReachNext
                # Adding this city to the queue
                q.append([nextStop, remainingStops - 1, priceToReachNext])

    return -1 if result[dst] == float("inf") else result[dst]
