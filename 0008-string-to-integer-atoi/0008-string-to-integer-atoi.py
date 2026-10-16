
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if num > INT_MAX // 10 or (
                num == INT_MAX // 10 and digit > 7
            ):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
