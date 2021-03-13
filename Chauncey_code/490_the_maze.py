from collections import deque
DIRECTIONS = {'left': -1, 'right': 1, 'up': -1, 'down': 1}


class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        queue = deque([tuple(start)])
        visited = set()
        visited.add(tuple(start))

        while queue:
            current_position = queue.popleft()
            if current_position == tuple(destination):
                return True

            for direction in DIRECTIONS:
                next_position = self.find_next_position(maze, current_position, direction)
                if next_position in visited:
                    continue
                queue.append(next_position)
                visited.add(next_position)

        return False


    def find_next_position(self, maze, start, direction):
        row, column = start[0], start[1]

        if direction in ['left', 'right']:
            rolling_area = maze[row]
            while 0 <= column < len(maze[0]) and rolling_area[column] != 1:
                column += DIRECTIONS[direction]
            return (row, column - DIRECTIONS[direction])

        elif direction in ['up', 'down']:
            rolling_area = [maze[i][column] for i in range(len(maze))]
            while 0 <= row < len(maze) and rolling_area[row] != 1:
                row += DIRECTIONS[direction]
            return (row - DIRECTIONS[direction], column)



obj = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]

print(obj.hasPath(maze, start, destination))