class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        output=[]
        start,end=intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= end:
                end = max(end, cur_end)
            else:
                output.append([start,end])
                start,end = cur_start, cur_end
        output.append([start,end])
        return output

                  

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        