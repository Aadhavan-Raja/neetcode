class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(' ', '')
        reverse = s[::-1]
        return s == reverse