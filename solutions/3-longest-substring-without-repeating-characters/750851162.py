class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        max_len=0
        visited=set()
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            visited.add(s[right])
            max_len=max(max_len,len(visited))
        return max_len
        """
        :type s: str
        :rtype: int
        """
        