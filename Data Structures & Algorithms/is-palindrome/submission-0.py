class Solution:
    # Solution 1: Build new string
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    # Time complexity: O(n) — one pass to build string, one pass to reverse and compare
    # Space complexity: O(n) — new string created, could be as long as original
    
    # Edge cases:
    # - Empty string: newStr is "" and "" == "" is True
    # - Only spaces or punctuation: newStr ends up empty, returns True
    # - Single character: always True
    # - Mixed case: handled by .lower()
