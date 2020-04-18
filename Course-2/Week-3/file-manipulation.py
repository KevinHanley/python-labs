filename = input("Enter file name: ")
filehandle = open(filename)

count = 0
total = 0

for line in filehandle :
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    count = count + 1 #counting the line

    position = line.find(':')
    right = line[position + 1:]
    strnumber = right.strip()

    fltnumber = float(strnumber)
    total = fltnumber + total

average = total/count
print('Average spam confidence:', average)
