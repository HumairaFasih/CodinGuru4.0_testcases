import random
import sys

T = int(input())

with open('input00.txt', 'w') as input_file:
    sys.stdout = input_file
    print(T)

    for i in range(T):
        n = random.randint(2, 20)
        print(n)
        for j in range(n):
            n_i = random.randint(1, 1000)
            print(n_i, end=" ")
        print()
