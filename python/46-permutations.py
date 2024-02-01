class Solution:
    
    # Initialize class with two attributes: a solution array
    # to keep track of current solutions within recursion tree; and 
    # a hashtable to keep track of numbers used when constructing the solution.
    def __init__(self):
        self.solution = []
        self.table = dict()

    def permute(self, nums: list[int]) -> list[list[int]]:
        
        # Backtracking function - generates all permutations.
        def backtrack(limit: int, array: list[int]):
            if len(array) >= limit:
                self.solution.append(array.copy())
            else:
                for i in range(limit):
                    if nums[i] not in self.table or self.table[nums[i]] is False:
                        array.append(nums[i])
                        self.table[nums[i]] = True
                        backtrack(limit, array)
                        self.table[nums[i]] = False
                        array.pop()
        
        # Initialize array and backtrack.
        array: list[int] = []
        backtrack(len(nums), array)
        return self.solution