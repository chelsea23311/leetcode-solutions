class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for word in strs:
            key_word=''.join(sorted(word))
            if key_word not in hashmap:
                hashmap[key_word]=[]
            hashmap[key_word].append(word)
        return list(hashmap.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        