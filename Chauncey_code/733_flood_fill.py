class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image

        self.bfs(image, sr, sc, color, newColor)
        # self.dfs(image, sr, sc, color, newColor)

        return image


    def bfs(self, image, sr, sc, color, new_color):
        queue = collections.deque([(sr, sc)])
        visited = set()

        while len(queue) > 0:
            sr, sc = queue.popleft()
            if image[sr][sc] != color:
                continue
            image[sr][sc] = new_color

            if sr - 1 >= 0:
                queue.append((sr - 1, sc))
            if sr + 1 < len(image):
                queue.append((sr + 1, sc))
            if sc - 1 >= 0:
                queue.append((sr, sc - 1))
            if sc + 1 < len(image[0]):
                queue.append((sr, sc + 1))


    def dfs(self, image, sr, sc, color, new_color):
        if image[sr][sc] == color:
            image[sr][sc] = new_color
            if sr - 1 >= 0:
                self.dfs(image, sr - 1, sc, color, new_color)
            if sr + 1 < len(image):
                self.dfs(image, sr + 1, sc, color, new_color)
            if sc - 1 >= 0:
                self.dfs(image, sr, sc - 1, color, new_color)
            if sc + 1 < len(image[0]):
                self.dfs(image, sr, sc + 1, color, new_color)