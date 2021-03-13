from collections import deque, defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        self.graph = defaultdict(list)
        for a, b in dislikes:
            self.graph[a].append(b)
            self.graph[b].append(a)

        self.color = {}
        return all(self.dfs(node) for node in range(1, N + 1) if node not in self.color)


    def dfs(self, node, c = 0):
        if node in self.color:
            return self.color[node] == c
        self.color[node] = c
        return all(self.dfs(neighbor, c ^ 1) for neighbor in self.graph[node])


obj = Solution()
N = 4
dislikes = [[1,2],[1,3],[2,4]]

print(obj.possibleBipartition(N, dislikes))