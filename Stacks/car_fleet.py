"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car
and speed[i] is the speed of the ith car (in miles per hour).
A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored
(i.e., they are assumed to have the same position).
A car fleet is some non-empty set of cars driving at the same position and same speed.
Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.


"""


def car_fleet(target, position, speed):
    # Time = Space = O(n)
    """
    Step 1: Find the time taken to reach the target for each car and sort the time in descending order
            (i.e nearest to target is at the end of the array).
    Step 2: We will start popping from the end of the array, that means the car which is nearest to the target,
            now if the time taken by the current car is less than its previous car, then we know that no car can overtake
            this car, so it alone forms a fleet.
            And if the previous car takes less time than the current car, it means that the preivous car and current car
            form a fleet, and therefore we let the previous car go, and keep the current car in the top of the stack.
    Step 3: Once there is just a single car in the stack, we break and return the result.

    """

    # Zipping cars position and speed
    cars = sorted(zip(position, speed))
    # Computing the time taken by each car to reach the target distance
    times = [float(target - p) / s for p, s in cars]
    fleet = 0  # result

    # If the stack contains more than one car
    while len(times) > 1:
        # Getting the car nearest to the target
        curr_car_time = times.pop()
        # If the current car takes less time to reach the target than the previous car
        if curr_car_time < times[-1]:
            # It forms a fleet
            fleet += 1
        else:
            # If the current car is slower than the previous car, then they form a fleet
            # We keep the slower car in the stack to compare it with other previosu car.
            times[-1] = curr_car_time

    return fleet + len(times)
