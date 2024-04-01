#multiply.py
#! /usr/bin/env python3
size = int(input("Enter the size of your table: "))

cell_width = len(str((size * size))) + 1
print(cell_width)

for i in range(1, size +1):
    for j in range(1, size + 1):
        print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end = " ")
        #print("{:4d}".format(i * j), end = " ")
    print()





### push to github
    ### email link to github too 