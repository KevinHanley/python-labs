filename = input("Enter file name: ")
fhandle = open(filename, 'r')
txtfile = fhandle.read()

txtfile = txtfile.rstrip()
print(txtfile.upper())
