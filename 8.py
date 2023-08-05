wait = 0
start = 1
end = 2

numDic = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
        }


class Solution:
    def __init__(self):
        self.status = wait
        self.ans = 0
        self.isNegative = False

    def getans(self) -> int:
        if self.isNegative:
            self.ans = -self.ans
        if self.ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if self.ans < -2 ** 31:
            return -2 ** 31
        return self.ans

    def myAtoi(self, s: str) -> int:
        for x in s:
            if x == "-":
                self.isNegative = True
                continue
            if x in numDic:
                self.status = start
                self.ans = self.ans * 10 + numDic[x]
            else:
                if x == " ":
                    if self.status == start:
                        return self.getans()
                    continue
                else:
                    self.status = wait
                    self.ans = 0
                    self.isNegative = False
                    return self.getans()

        return self.getans()

    def check_status(self):
        if self.status == wait:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    # print(s.myAtoi("42"))
    # print(s.myAtoi("   -42"))
    # print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    # print(s.myAtoi("-91283472332"))
    # print(s.myAtoi("+-12"))
    # print(s.myAtoi("  0000000000012345678"))
    # print(s.myAtoi("  00000000000"))
