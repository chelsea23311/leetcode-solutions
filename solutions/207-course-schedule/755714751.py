class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        visited=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        for ai,bi in prerequisites:
            graph[bi].append(ai)
        path=[0]*numCourses
        def dfs(course,path):
            if visited[course]==1:
                return True
            path[course]=1
            visited[course]=1
            for x in graph[course]:
                if path[x]==1:
                    return False
                else:
                    if dfs(x,path):
                        continue
                    else:
                        return False
            path[course]=0
            return True
        for i in range(numCourses):
           
            if not dfs(i,path):
                return False
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        