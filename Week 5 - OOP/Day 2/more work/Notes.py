# Solution to previous day daily challenge - finding subsets in lists and manipulating them

from itertools import combinations

class Subsets:

    def __init__(self, nums):
        self.nums = nums

    def find_zero_sum(self):
        subsets = combinations(self.nums, 3)
        return list(filter(lambda x: sum(x) == 0, subsets))

s = Subsets([-25, -10, -7, -3, 2, 4, 8, 10])

print(s.find_zero_sum())