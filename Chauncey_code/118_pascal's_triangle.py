class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        output = [[1]]

        for _ in range(2, numRows + 1):
            new_row = self.get_next_row(output[-1])
            output.append(new_row)

        return output

    def get_next_row(self, row):
        n = len(row)
        new_row = [0] * (n + 1)
        new_row[0] = 1
        new_row[n] = 1

        for i in range(1, n):
            new_row[i] = row[i - 1] + row[i]

        return new_row