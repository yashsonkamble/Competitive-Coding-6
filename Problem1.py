"""
I used a backtracking approach that tries all possible permutations, so the time complexity is O(n!) in the worst case. The space complexity is O(n) due to the recursion stack and the array used to track the current permutation."
"""
class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        combination = [i for i in range(n + 1)]  # 1-based indexing
        self.backtrack(combination, 1)
        return self.count

    def backtrack(self, combination: list, index: int):
        if index >= len(combination):
            self.count += 1
            return
        for i in range(index, len(combination)):
            self.swap(combination, i, index)
            if combination[index] % index == 0 or index % combination[index] == 0:
                self.backtrack(combination, index + 1)
            self.swap(combination, i, index)

    def swap(self, combination: list, i: int, j: int):
        combination[i], combination[j] = combination[j], combination[i]