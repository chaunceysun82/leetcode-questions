logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

letter_list = []
digit_list = []

for log in logs:
    if log.split()[1].isdigit():
        digit_list.append(log)
    else:
        letter_list.append(log)

sorted_letter_list = sorted(letter_list, key = lambda log: (log.split()[1:], log.split()[0]))
print(sorted_letter_list + digit_list)