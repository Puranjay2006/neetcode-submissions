class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

# Time complexity: O(n) — one pass through the array, each hashmap lookup is O(1)
# Space complexity: O(n) — worst case every element stored in hashmap before answer found

# Edge cases:
# - Same number used twice: [3,3] target=6 — works because map is checked before adding
# - Negative numbers — works fine
# - Two elements only — works fine