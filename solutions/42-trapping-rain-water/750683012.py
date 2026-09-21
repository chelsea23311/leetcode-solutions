class Solution(object):
    def trap(self, height):
        water=0
        max_left,max_right=height[0],height[-1]
        left_index,right_index=0,len(height)-1
        while left_index<=right_index:
            if max_left<=max_right :
                if height[left_index]<max_left:
                     water+=max_left-height[left_index]
                max_left=max(height[left_index],max_left)
                left_index+=1
            else:
                if height[right_index]<max_right:
                    water+=max_right-height[right_index]
                max_right=max(height[right_index],max_right)
                right_index-=1
        return water
            





        """
        :type height: List[int]
        :rtype: int
        """
        