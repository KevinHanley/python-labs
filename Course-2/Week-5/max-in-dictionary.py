name = input("Enter file name:")
handle = open(name)

senders = dict()

for line in handle :
    if not line.startswith('From ') :
        continue

    words = line.split()
    secondword = words[1]

    senders[secondword] = senders.get(secondword,0) + 1

maxkey = None
maxvalue = None

for k,v in senders.items() :
    if maxvalue is None or v > maxvalue :
        maxkey = k
        maxvalue = v

print(maxkey, maxvalue)
