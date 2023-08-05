class Solution:
    def reverse(self, x: int) -> int:
        t = 0
        isNegative = False
        while x != 0:
            if x < 0:
                isNegative = True
                x = -x
            t = t * 10 + x % 10
            x = int(x / 10)
        if isNegative:
            t = -t
        if t > 2 ** 31 - 1 or t < -2 ** 31:
            return 0

        return t


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(0))
    print(s.reverse(1534236469))