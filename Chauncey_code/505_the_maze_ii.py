from collections import deque
DIRECTIONS = {'left': -1, 'right': 1, 'up': -1, 'down': 1}


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = deque([(tuple(start), 0)])
        min_distance = {tuple(start): 0}

        while queue:
            current_position, distance = queue.popleft()

            for direction in DIRECTIONS:
                next_position, step = self.find_next_position(maze, current_position, direction)
                if next_position in min_distance and distance + step >= min_distance[next_position]:
                    continue
                queue.append((next_position, distance + step))
                min_distance[next_position] = distance + step 

        if tuple(destination) in min_distance:
            return min_distance[tuple(destination)]

        return -1


    def find_next_position(self, maze, start, direction):
        row, column = start[0], start[1]

        if direction in ['left', 'right']:
            rolling_area = maze[row]
            step = 0
            while 0 <= column < len(maze[0]) and rolling_area[column] != 1:
                column += DIRECTIONS[direction]
                step += 1
            return (row, column - DIRECTIONS[direction]), step - 1

        elif direction in ['up', 'down']:
            rolling_area = [maze[i][column] for i in range(len(maze))]
            step = 0
            while 0 <= row < len(maze) and rolling_area[row] != 1:
                row += DIRECTIONS[direction]
                step += 1
            return (row - DIRECTIONS[direction], column), step - 1