class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if  rowIndex == 0:
            return [1]

        res = [1]
        for _ in range(1, rowIndex + 1):
            res = self.get_next_row(res)

        return res

    def get_next_row(self, row):
        n = len(row)
        new_row = [0] * (n + 1)
        new_row[0] = 1
        new_row[n] = 1

        for i in range(1, n):
            new_row[i] = row[i - 1] + row[i]

        return new_row