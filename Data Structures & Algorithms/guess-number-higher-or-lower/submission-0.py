# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n # l = 1 since the range starts from 1 to n 
        while True:
            m = (l + r) // 2
            res = guess(m) #guess func is already defined and returns 0 if guess==pick
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m