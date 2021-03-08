import collections
class Solution:
    def minimumSemesters(self, n: int, relations) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for relation in relations:
            graph[relation[0]].append(relation[1])

        indegrees = self.get_indegree(graph)

        start_nodes = [x for x in graph if indegrees[x] == 0]
        queue = collections.deque(start_nodes)

        step = 0
        visited_count = 0
        while queue:
            step += 1
            next_queue = []

            for node in queue:
                visited_count += 1

                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        next_queue.append(neighbor)

            queue = next_queue

        return step if visited_count == n else -1


    def get_indegree(self, graph):
        indegrees = collections.defaultdict(int)

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees


obj = Solution()
n = 5
relations = [[1,3],[2,3],[2,4],[3,5],[4,5]]

print(obj.minimumSemesters(n, relations))















