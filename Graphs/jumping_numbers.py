"""
A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is
not considered as 1.
All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but
796 and 89098 are not.

Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can
be printed in any order.

"""


def jumpingNumbers(x):
    # Time = Space = O(k), k = number of jumping numbers
    """
    Logic: All single digit numbers are considered as Jumping numbers. And we continue to generate the rest of the
    numbers using these numbers. We use BFS, we store [1-9] in the queue, and keep popping the numbers and add
    it to the result, and then we try to find the next jumping number using it.
    The main part is to figure out the formula for the next jumping number.

    If the last digit of the current number is = 0 or 9, then we can only generate one jumping number, else
    we can generate two jumping numbers.
    Ex: For number 2, since the last digit is not 0 or 9,
    jumping_number_1 = 2*10 + ((2%10) + 1) = 23
    jumping_number_2 = 2*10 + ((2%10) - 1) = 21
    Formula = curr_number * 10 + ((curr_number % 10) + 1) and curr_number * 10 + ((curr_number % 10) - 1)

    """

    # Initializing the queue with all single-digit numbers.
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []  # To store all the jumping numbers <= x

    # BFS
    while q:
        curr = q.pop()
        # Appending the current jump number to the result
        result.append(curr)
        # If the current jump number's last digit is 0, then we can only increase to + 1
        if curr % 10 == 0:
            next_number = curr * 10 + 1
            # Add this next number to queue only if its <= x
            if next_number <= x:
                q.append(next_number)
        # If the current jump number's last digit is 9, then we can only decrease by -1
        elif curr % 10 == 9:
            next_number = curr * 10 + 8
            if next_number <= x:
                q.append(next_number)
        else:
            # General case: We can have two jumping numbers, by increasing and decreasing.
            next_number_one = curr * 10 + ((curr % 10) + 1)
            next_number_two = curr * 10 + ((curr % 10) - 1)
            if next_number_one <= x and next_number_two <= x:
                q.append(next_number_one)
                q.append(next_number_two)
    return result


print(jumpingNumbers(120))
