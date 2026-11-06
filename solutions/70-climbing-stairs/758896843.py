class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            i1,i2=1,2
            for _ in range(n-2):
                i3=i1+i2
                i1=i2
                i2=i3
            return i3
            

        """
        :type n: int
        :rtype: int
        """
        