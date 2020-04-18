fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line.rstrip()
    pieces = line.split()

    for piece in pieces :
        if piece not in lst:
            lst.append(piece)

lst.sort()
print(lst)
