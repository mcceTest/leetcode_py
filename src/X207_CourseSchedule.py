'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0 or not prerequisites:
            return True

        g, indegree = self.adjList(numCourses, prerequisites)

        for _ in range(numCourses):
            # find one node with indegree 0 and remove it
            curIdx = 0
            while curIdx < numCourses and indegree[curIdx] != 0:
                curIdx += 1

            if curIdx == numCourses:
                return False

            # so not to consider this node again
            indegree[curIdx] = -1
            
            for neig in g[curIdx]:
                indegree[neig] -= 1

        return True



    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0 or not prerequisites:
            return True

        g, indegree = self.adjList(numCourses, prerequisites)

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for neig in g[cur]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    q.append(neig)

        return count == numCourses

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
        numCourses = 3
        prerequisites = [[1,0],[0,1]]
        
        print(sol.canFinish(numCourses, prerequisites))
        
        

if __name__ == "__main__":
    Solution.main()