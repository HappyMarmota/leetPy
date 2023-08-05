class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = {}
        d = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i], []) + [i]
            d[s[i]] = m[s[i]][-1] - m[s[i]][0]
        print(m)
        print(d)
        for k, v in m.items():
            if len(v) > 1:
                for i in range(len(v)):
                    for j in range(i + 1, len(v)):
                        if self.isTrue(s[i:j]):
                            return s[i:j]

    def isTrue(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    str = "babad"
    s = Solution()
    print(s.longestPalindrome(str))
