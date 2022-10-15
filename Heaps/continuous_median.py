"""
Write a ContinuousMedianHandler class that supports:
1. The continuous insertion of numbers with the insert method.
2. The instant retrieval of the median of the numbers that have been inserted this far with the getMedian method.

"""


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.lowers = None
        self.greaters = None

    def insert(self, number):
        # Time: O(logn) and Space: O(n)
        """
        Logic:
        We will maintain two heaps, lowers = max heap and greaters = min heap.
        As we insert the numbers, the center value gives the median, which will come from the max of the lowers
        and min of the greaters heaps respectively.
        After inserting the numbers, we will re-balance the heaps so that we can calculate the median.
        After re-balancing, we will update the median for the current inserted numbers.
        """
        # If the lowers heap is empty or the number if smaller than the top value of the lowers heap then we will
        # insert it in lowers.
        if not self.lowers or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            # Else, insert in greaters heap.
            self.greaters.insert(number)

        # We rebalance and update the median.
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        # To rebalance heap, we will check the difference between the lengths of the two heaps,
        # Whichever heap has greater than 1 elements, we will pop it and insert it into the other heap.
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self):
        # If the both the heaps have the same length, we will simple take the average of the middle two elements.
        # Else whichever heap has greater length, we will return its top value.
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median
