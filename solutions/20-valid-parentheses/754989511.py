class Solution(object):
    def isValid(self, s):
        hashmap={')':'(',']':'[','}':'{'}
        stack=[]
        for word in s:
            if word in hashmap:
                if stack and stack[-1]==hashmap[word]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(word)
        return len(stack)==0

        """
        :type s: str
        :rtype: bool
        """
        