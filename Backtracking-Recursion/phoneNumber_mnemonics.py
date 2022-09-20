"""
Given a phone number as a string, find all the possible mnemonics/combinations of the letters possible using the
keypad.
Since numbers 1 and 0, don't have any letters associated with them in the keypad, so keep them as they are.

Input: "1905"
Output: ['1w0j', '1w0k', '1w0l', '1x0j', '1x0k', '1x0l', '1y0j', '1y0k', '1y0l', '1z0j', '1z0k', '1z0l']

"""


def phoneNumberMnemonics(phoneNumber):
    # Time = Space = O(4^n * n), 4^n because for each number we can at max make 4 recursive calls,
    # so for n numbers, we make 4^n calls.
    """
    Logic:
    In the function call, start with the first number, if the number is 0 or 1 then just add it to the stack,
    else, loop all the letters associated with the number and for every letter, add it to the stack and again
    make a new call moving to the next number.
    If the next number' idx == len(phoneNumber) then we know the current configuration of the stack can be added
    to the result, and we return.
    After finishing the function call for every letter, we remove it from the stack to find the next configuration.
    """

    # Creating the numbers dictionary for accessing all the letters associated with a number on the keypad.
    numbers = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    # Storing the results.
    result = []
    # Start of the function call
    solve(phoneNumber, [], numbers, 0, result)

    return result


def solve(phoneNumber, stack, numbers, idx, result):
    # If the current number idx is out of bounds, then we add the current stacks configuration to the result array.
    if idx == len(phoneNumber):
        result.append(''.join(stack))
        return

    # If the current number is 0 or 1, then we add it to the stack directly and move to the next number.
    if phoneNumber[idx] == '0' or phoneNumber[idx] == '1':
        stack.append(phoneNumber[idx])
        solve(phoneNumber, stack, numbers, idx + 1, result)
        stack.pop()
    else:
        # Else, We loop every letter associated with the current number, add it, make a new call, pop it.
        for letter in numbers[phoneNumber[idx]]:
            stack.append(letter)
            # Moving to the next number.
            solve(phoneNumber, stack, numbers, idx + 1, result)
            stack.pop()


print(phoneNumberMnemonics('1905'))
