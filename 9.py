class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == self.reverse_int(x):
            return True
        else:
            return False

    def reverse_int(self, i: int) -> int:
        r = 0
        while i != 0:
            r = r * 10 + i % 10
            i = int(i / 10)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(-101))
