#! /usr/bin/env python3
import argparse

def get_args():
    #create an argumentparser object
    parser = argparse.ArgumentParser(description= 'This script returns the Fibonacci number at \
                                     at a specified location in the Fibonnaci sequence.')
    #add positional arguments (these are the ones that are absolutley essential/required)
    parser.add_argument("num", help = "The Fibonnaci number you wish to calculate", type = int)

    # add optional arguments:
    # if 'store_true', this means assign 'True' if the argument is specified on the command
    #line, so the default of 'store_true' is false
    parser.add_argument("-v", "--verbose", help="Print verbose output or not", action='store_true')

    #parse the actual arguments
    args = parser.parse_args()

    return args


def fib(n):
#initializes variables 
    a,b = 0,1

#calculate
    for i in range(int(n)):
        a,b = b, a+b

#store results
    fibonacci_number = a
    return fibonacci_number

def print_output(number, fibonacci_number):
#print output
    if args.verbose:
        print('The Fibonacci number for', number, 'is:',fibonacci_number )
    else:
        print(fibonacci_number)

def main():
    #calculate fibonacci number
    fibonacci_number = fib(args.num)
    print_output(args.num, fibonacci_number) 


#get the command line arguments
args = get_args()

if __name__ == '__main__':
    main()
