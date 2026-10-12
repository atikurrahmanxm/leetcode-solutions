class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0  # Track the best palindrome's boundaries
        
        def expand(left, right):
            # Expand while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1
        
        for i in range(len(s)):
            # Odd-length palindrome centered at i
            len1 = expand(i, i)
            # Even-length palindrome centered between i and i+1
            len2 = expand(i, i + 1)
            
            max_len = max(len1, len2)
            
            if max_len > end - start:
                # Compute new start/end from center i and length
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    