from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:

        structure = defaultdict(list)
        for id, manager_id in enumerate(manager):
            if manager_id != -1:
                structure[manager_id].append((id, informTime[id]))

        queue = deque([(headID, informTime[headID])])
        max_time = 0

        while queue:
            employee_id, current_time = queue.popleft()

            if not structure[employee_id]:
                continue

            max_time = max(max_time, current_time)

            for subordinate in structure[employee_id]:
                queue.append((subordinate[0], subordinate[1] + current_time))

        return max_time


n = 11
headID = 4
manager = [5,9,6,10,-1,8,9,1,9,3,4]
informTime = [0,213,0,253,686,170,975,0,261,309,337]

obj = Solution()
print(obj.numOfMinutes(n, headID, manager, informTime))

