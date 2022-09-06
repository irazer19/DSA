"""
You need to make maximum profit by doing k transactions. You can only do one transaction per day.

"""


def maxProfitWithKTransactions(prices, k):
    # Time = Space = O(nk)

    """
    Idea: Either we can do the transaction today or keep the last daya's profit.
    If we do the transaction today, the profit = current days purchase price + max(last transactions profit.)
    """
    # Base case
    if k == 0 or not prices:
        return 0
    # Using DP, rows = number of transactions, columns = prices on each day.
    # Each cell represents: the max profit for ith transaction on jth day
    # 1st row and 1st col will be 0 because we cannot make profit for 0 transactions
    store = [[0 for _ in prices] for _ in range(k + 1)]

    # Starting with 1 transaction.
    for i in range(1, len(store)):
        # We will keep track of the max profit we made on last transaction till previous day.
        max_prev_trans = float('-inf')
        # Starting from day 1
        for j in range(1, len(store[0])):
            # Calculating the max profit till previous day, either existing profit is greater OR
            # the immediately previous day profit maybe greater.
            max_prev_trans = max(max_prev_trans, store[i - 1][j - 1] - prices[j - 1])
            # Calculating the max profit for today with jth transaction.
            # Which is = max(We dont do the transaction, We do the transaction)
            store[i][j] = max(store[i][j - 1], max_prev_trans + prices[j])

    # Max profit with kth transaction on nth day
    return store[-1][-1]


print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2))
