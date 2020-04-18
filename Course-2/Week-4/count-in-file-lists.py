fname = input("Enter file name: ")
fh = open(fname)

count = 0

for line in fh :
    line.rstrip()

    if not line.startswith('From') :
        continue

    if line.startswith('From:') :
        continue

    b = line.split()
    print(b[1])
    count = count + 1


print("There were", count, "lines in the file with From as the first word")
