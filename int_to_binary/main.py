from math import trunc

i = 15
output = ''
while i != 1:
    if i % 2 == 0:
        output += '0'
        i = i / 2
    else:
        output += '1'
        i = trunc(i/2)

        
output += '1'
print(output)

