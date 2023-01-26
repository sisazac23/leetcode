# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while True:
            mid = (low+high)//2
            if isBadVersion(mid)==True and isBadVersion(mid-1)==False:
                return mid
            if isBadVersion(mid)==False and isBadVersion(mid-1)==False:
                low = mid+1
            if isBadVersion(mid)==True and isBadVersion(mid-1)==True:
                 high = mid -1 
        return mid
        