import random
import sys

T = int(input())

with open('input02.txt', 'w') as input_file:
    sys.stdout = input_file
    print(T)

    for i in range(T):
        m = random.randint(1,100)
        print(m)
        for j in range(m):
            n_i = random.randint(1,20)
            print(n_i, end=" ")
        print()
    