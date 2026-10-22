class Solution:
    def isPalindrome(self, s: str) -> bool:
        fil_s="".join(char.lower() for char in s if char.isalnum())
        return fil_s==fil_s[::-1]
