"""
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent
posts have the same color.
"""


def paintFence(n, k):
    # Time = Space = O(n)
    """
    Logic: Since at most two posts can have the same color, we start the problem from fence 2 because the problem
    is not defined for fence 0 and 1.
    We have two lists: same and diff.

    same = Stores all the ways where the last two posts have the same color.
    diff = Stores all the ways where the last two posts have different color.
    total = same + diff, this list holds the final answer.

    For the same color for the last two posts, we store the previous posts diff as the answer(we don't use the
    previous same because that will result in three consecutive same posts, so we use only the diff and add the
    same color)

    For the diff color for the last two posts, we take the previous total * (k - 1), since we have to use a
    different color, we take total of the previous post and except that color we use all other colors, and that's
    why we use (k - 1).

    """
    # Initializing same, diff and total for each post.
    same = [0 for _ in range(n + 1)]
    diff = [0 for _ in range(n + 1)]
    total = [0 for _ in range(n + 1)]

    # The questions is invalid for post 0 and 1, so we start with post 2.
    # In post 2, for same color, we have k options, and for different color we have k * (k - 1) options.
    # k (post 1 can be painted in k colors) * (k - 1) (except post 1 color, we can use all other colors.)
    same[2] = k
    diff[2] = k * (k - 1)
    total[2] = same[2] + diff[2]

    # Starting the problem with post 3.
    for i in range(3, n + 1):
        # same = previous posts different.
        same[i] = diff[i - 1]
        # diff = previous posts total * all other colors except the previous color.
        diff[i] = total[i - 1] * (k - 1)
        total[i] = same[i] + diff[i]

    return total[n]


print(paintFence(3, 2))
