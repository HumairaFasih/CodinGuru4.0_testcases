import random
import sys

# write the output to an input file instead of the terminal
with open('Sample_input_q5.txt', 'w') as input_file:
    sys.stdout = input_file
    def func(counter):

        #generate three space-separated integers and print them
        m = random.randint(1,10)
        n = random.randint(1,10)
        o = random.randint(1,10)
        print(m,n,o)

        #In the next line, print another random integer - called lf
        k = random.randint(1,10)
        print(k)

        #print lf lines, each containing a random integer and one word (from green and red, chosen randomly as well)
        for i in range(1,k+1):
            d = random.randint(1, 100)
            word = random.choice(['green','red'])
            print(d,word)


    t = int(input())
    print(t)

    for i in range(1,t+1):
        func(i)

# input format description from the Question
# The first line of the input gives the number of test cases, T. T test cases follow.
# The first line of each test case contains three space-separated integers: M, the number of balls to be painted red
# N, the number of balls to be painted green
# O, the number of balls that can be painted in either of the two colors.
#  The next line contains one integer k, which specifies the number of paint packets in the price list. 
# After the first two lines, k lines follow each containing one integer - representing the cost of the paint packet - followed by a string describing the color of the paint.
#  Only relevant colors are provided. 
