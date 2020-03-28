'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
import collections

class Solution(object):
    STATUS_UNVISITED = 0
    STATUS_VISITING = 1
    STATUS_VISITED = 2
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []

        g, _ = self.adjList(numCourses, prerequisites)
        visitStatus = [self.STATUS_UNVISITED] * numCourses

        res = []
        for num in range(numCourses):
            if not self.dfs(numCourses, g, num, visitStatus, res):
                return []
        
        res.reverse()
        return res
        
    def dfs(self, numCourses, g, curCourse, visitStatus, res):
        if visitStatus[curCourse] == self.STATUS_VISITED:
            return True

        if visitStatus[curCourse] == self.STATUS_VISITING:
            return False
        

        visitStatus[curCourse] = self.STATUS_VISITING
        for neig in g[curCourse]:
            if not self.dfs(numCourses, g, neig, visitStatus, res):
                return False

        visitStatus[curCourse] = self.STATUS_VISITED
        res.append(curCourse)

        return True


    def findOrder3(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []

        g, _ = self.adjList(numCourses, prerequisites)
        visited = [False] * numCourses
        visiting = [False] * numCourses

        res = []
        for num in range(numCourses):
            if not self.dfs3(numCourses, g, num, visited, visiting, res):
                return []
        
        res.reverse()
        return res
        
    def dfs3(self, numCourses, g, curCourse, visited, visiting, res):
        if visited[curCourse]:
            return True

        if visiting[curCourse]:
            return False

        visiting[curCourse] = True
        for neig in g[curCourse]:
            if not self.dfs3(numCourses, g, neig, visited, visiting, res):
                return False

        visiting[curCourse] = False
        visited[curCourse] = True
        res.append(curCourse)

        return True


    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []

        g, indegree = self.adjList(numCourses, prerequisites)

        q = collections.deque()
        for num in range(numCourses):
            if indegree[num] == 0:
                q.append(num)

        res = []
        while q:
            head = q.popleft()
            res.append(head)
            for neig in g[head]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    q.append(neig)

        if len(res) == numCourses:
            return res
        else:
            return []


    def adjList(self, numCourses, prerequisites):
        g = {}
        indegree = [0] * numCourses
        for i in range(numCourses):
            g[i] = set()

        for src, dep in prerequisites:
            g[dep].add(src)
            indegree[src] += 1

        return g, indegree
        

    @staticmethod
    def main():
        sol = Solution()
        numCourses = 2
        prerequisites = [[1,0]]
        
        print(sol.findOrder(numCourses, prerequisites))
        
        

if __name__ == "__main__":
    Solution.main()