class Solution(object):
    def minWindow(self, s, t):
        def check(s_dict,t_dict):
            for key in t_dict:
                if s_dict.get(key,0) >= t_dict[key]:
                    continue
                return False
            return True
        left = 0
        s_dict, t_dict = {}, {}
        min_len = float('inf')
        res = ""
        for c in t:
            t_dict[c] = t_dict.get(c,0)+1
        
        for right in range(len(s)):
            s_dict[s[right]] = s_dict.get(s[right],0)+1
            while check(s_dict, t_dict):
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res = s[left:right+1]
                s_dict[s[left]] -= 1
                left += 1
        return res


            


        """
        :type s: str
        :type t: str
        :rtype: str
        """
        