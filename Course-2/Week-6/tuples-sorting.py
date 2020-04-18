name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mylist = list()
for line in handle :
    if not line.startswith('From ') :
        continue

    words = line.split()
    fulltime = words[5]

    ftime = fulltime.split(':')
    test = ftime[0]
    mylist.append(test)

list2 = dict()
for item in mylist :
    list2[item] = list2.get(item,0) + 1

for k,v in sorted(list2.items()):
    print(k,v)
