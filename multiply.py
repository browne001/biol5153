#multiply.py
#! /usr/bin/env python3

def get_input():

    #ask for size of matrix
    size = int(input("Enter the size of your table: "))
    return size

def print_table(n): 
# calculate the spaces we will need for the output of each cell
    cell_width = len(str((n * n))) + 1
    print(cell_width)

#nested for loop
    for i in range(1, n +1):
        for j in range(1, n + 1):
            print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end = " ")
        #print("{:4d}".format(i * j), end = " ")
        print()


def main():
    input_num = get_input()

    print_table(input_num)

if __name__ == '__main__':
    main()



### push to github
    ### email link to github too 