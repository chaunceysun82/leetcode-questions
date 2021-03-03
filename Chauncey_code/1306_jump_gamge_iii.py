class Solution:
    def canReach(self, arr, start) -> bool:
        visited = set()
        return self.dfs(arr, start, visited)

    def dfs(self, arr, index, visited):
        if arr[index] == 0:
            return True

        if index in visited:
            return False

        visited.add(index)

        next_index_1 = index + arr[index]
        next_index_2 = index - arr[index]

        if self.is_valid(next_index_1, arr) and self.is_valid(next_index_2, arr):
            return self.dfs(arr, next_index_1, visited) or self.dfs(arr, next_index_2, visited)
        elif self.is_valid(next_index_1, arr):
            return self.dfs(arr, next_index_1, visited)
        elif self.is_valid(next_index_2, arr):
            return self.dfs(arr, next_index_2, visited)

    def is_valid(self, index, arr):
        return index >= 0 and index <= len(arr) - 1



obj = Solution()
arr = [4,4,1,3,0,3]
start = 2
print(obj.canReach(arr, start))