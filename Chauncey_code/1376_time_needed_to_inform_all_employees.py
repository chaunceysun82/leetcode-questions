import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        structure = {id : [] for id in range(n)}
        for id, manager_id in enumerate(manager):
            if manager_id != -1:
                structure[manager_id].append(id)
        
        print(structure)

        queue = collections.deque([headID])
        total_time_needed = 0

        while len(queue) > 0:
            employee_num = len(queue)
            time_needed = 0
            for _ in range(employee_num):
                employee_id = queue.popleft()
                time_needed = max(time_needed, informTime[employee_id])

                if not structure[employee_id]:
                    continue

                for subordinate_id in structure[employee_id]:
                    queue.append(subordinate_id)

            total_time_needed += time_needed

        return total_time_needed


n = 11
headID = 4
manager = [5,9,6,10,-1,8,9,1,9,3,4]
informTime = [0,213,0,253,686,170,975,0,261,309,337]

obj = Solution()
print(obj.numOfMinutes(n, headID, manager, informTime))
