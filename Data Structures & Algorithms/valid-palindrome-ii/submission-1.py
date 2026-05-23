class Solution:
    def palindrome(self, s, left, right):
        while left < right:
            while left < right and s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left] != s[right]:
                return self.palindrome(s, left+1, right) or self.palindrome(s, left, right-1)
            left, right = left+1, right-1
        return True