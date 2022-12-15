"""
Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the
final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so
fairly by giving them arbitrary! rewards following two rules:
1. All students must receive at least one reward.
2. Any given student must receive strictly more rewards than an adjacent student (a student immediately to the left
or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score

Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to
students to satisfy the two rules.

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output: 25

"""


def minRewards(scores):
	# Time = Space = O(n)
	"""
	Logic:
	By default we will give 1 reward to each student.
	First we will move from left to right, if the current score is greater than the previous score, then we will
	add +1 to the current reward.
	Now we will move from right to left, if the current score is greater than its next score, then we will
	update the reward for the current student by = max(existing reward, 1 + reward of the next student)
	We use the max function because while visiting from left to right, we had already updated the rewards,
	so we don't want to change that as it represents the minimum reward for the students.
	"""
	# Initializing the reward result array, by default every student will get 1
	result = [1 for _ in scores]
	# Moving from left to right
	for i in range(1, len(scores)):
		# We compare the current score and the previous score.
		if scores[i] > scores[i - 1]:
			# Updating the reward for the current student.
			result[i] = result[i - 1] + 1
	# Now moving from right to left
	for i in range(len(scores) - 2, -1, -1):
		# We compare the current score with its immediate next score.
		if scores[i] > scores[i + 1]:
			result[i] = max(result[i], result[i + 1] + 1)
	# Returning the sum of the rewards given.
	return sum(result)
