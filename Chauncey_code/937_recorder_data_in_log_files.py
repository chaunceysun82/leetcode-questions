class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split(' ')[1].isalpha():
                letter_logs.append(log)
            if log.split(' ')[1].isdigit():
                digit_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ')[0]))

        return letter_logs + digit_logs


if __name__ == '__main__':
    obj = Solution()
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    res = obj.reorderLogFiles(logs)
    print(res)