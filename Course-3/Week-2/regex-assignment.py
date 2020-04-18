import re
handle = open('regex_sum_448517.txt')

total = 0

for line in handle :
    line = line.rstrip()

    x = re.findall('[0-9]+', line)

    for number in x :
        y = float(number)
        total = total + y

print(total)
