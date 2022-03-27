import random
import sys

T = int(input())

with open('Sample_input_q1.txt', 'w') as input_file:
    sys.stdout = input_file
    print(T)

    for i in range(T):
        p = random.randint(1, 15)
        print(p)
        for j in range(p):
            a_i = random.randint(1, 100)
            print(a_i, end=" ")
        print()
