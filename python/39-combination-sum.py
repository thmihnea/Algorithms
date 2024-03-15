from typing import List, Dict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Generate required data structures.
        solutions: Dict[str, bool] = dict()
        solution: List[int] = []

        def permute(solution: List[int], current_sum: int):
            """
            This function permutes through all possible combinations
            adding up to the target sum. If such a combination is found,
            then the result is added to the hashtable created above as
            a tuple (which is a hashable type in Python), and then we can
            simply keep track of all the different solutions we generated,
            irrespective of the order in which elements appear.
            """
            nonlocal target, candidates, solutions
            if current_sum == target:
                sorted_solution = tuple(sorted(solution))  
                solutions[sorted_solution] = True 
            else:
                for i in range(len(candidates)):
                    candidate: int = candidates[i]
                    if current_sum + candidate > target:
                        continue
                    solution.append(candidate)
                    permute(solution, current_sum + candidate)
                    solution.pop()
        
        # Call the function to permute all possible solutions.
        permute(solution, 0)

        # Simply return the output. Note that we can just generate
        # the solutions from the dictionary we previously created.
        return [list(solution) for solution in solutions.keys()]
        