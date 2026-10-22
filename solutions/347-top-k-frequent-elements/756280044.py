class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap={}
        for number in nums:
            if number not in hashmap:
                hashmap[number]=1
            else:
                hashmap[number]+=1
        number_list=[(num,v) for num,v in hashmap.items()]
        n = len(number_list)
        def part(left,right):
            key,target=number_list[left]
            while left<right:
                while left<right and number_list[right][1] > target:
                    right-=1
                number_list[left]=number_list[right]
                while left<right and number_list[left][1] <= target:
                    left+=1
                number_list[right]=number_list[left]
            number_list[left]=(key,target)
            return left
        def quicksort(l,r):
            if l>=r:
                return
            pos=part(l,r)
            if pos == n - k:
                return 
            elif pos > n - k:
                quicksort(l,pos-1)
            else:
                quicksort(pos+1,r)
        quicksort(0,n-1)
        return [t[0] for t in number_list[-k:]]

            


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        