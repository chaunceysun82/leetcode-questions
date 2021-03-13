import heapq

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        start = (0, 0)
        end = (len(A) - 1, len(A[0]) - 1)
        min_num = A[0][0]

        heap = []
        heapq.heappush(heap, (-A[0][0], start))
        visited = set()

        while heap:
            num, position = heapq.heappop(heap)
            min_num = min(min_num, -num)
            visited.add(position)

            if position == end:
                return min_num

            for direction in DIRECTIONS:
                next_x = position[0] + direction[0]
                next_y = position[1] + direction[1]
                if next_x < 0 or next_x >= len(A) or next_y < 0 or next_y >= len(A[0]) or (next_x, next_y) in visited:
                    continue

                heapq.heappush(heap, (-A[next_x][next_y], (next_x, next_y)))

        return -1