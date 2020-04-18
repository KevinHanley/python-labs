text = "X-DSPAM-Confidence:    0.8475";
number = text.find(':')

strNumber = text[number + 1:]
strNumber.lstrip()
fltNumber = float(strNumber)

print(fltNumber)
