from collections import deque

class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if int(grid[i][j]) and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        DIRECTIONS = [(1, 0), (-1 , 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y

                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False

        return int(grid[x][y])


if __name__ == '__main__':
    obj = Solution()
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]

    print(obj.numIslands(grid))
