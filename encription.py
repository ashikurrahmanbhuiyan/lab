a = input("Enter the string: ")

b = ''

for i in range(len(a)):
    c = format(ord(a[i]), '08b')
    for j in range(len(c)):
        b = b + c[j]


b = b + '1'
for i in range(len(b)+1,(505)):
    b = b + '0'

# 8 bit binary of length of string

c = format(len(a)*8, '08b')
for i in range(len(c)):
    b = b + c[i]



# 2d array of 32 bits

md = []
for i in range(0,len(b),32):
    md.append(b[i:i+32])

for i in range(len(md)):
    print(md[i])
