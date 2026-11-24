class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if x < 0:
            res = -res
        return res if -2**31 <= res <= 2**31 - 1 else 0