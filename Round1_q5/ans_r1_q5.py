
import sys

with open('Sample_output_q5.txt', 'w') as output_file:
    sys.stdout = output_file
    T = int(input())
    ans_array = []
    for testcase in range(T):
        c = list(map(int, input().split()))
        m = int(input())
        a = []
        for i in range(m):
            n, t = input().split()
            a.append((int(n), int(t == "green")))
        a.sort()
        res = 0
        b = [0] * 3
        for n, t in a:
            if c[t]-b[t] > 0:
                b[t] += 1
                res += n
            elif c[2]-b[2] > 0:
                b[2] += 1
                res += n
        ans_tuple = (sum(b), res)
        ans_array.append(ans_tuple)
    for i in range(len(ans_array)):
        print(f"Case #{i + 1}:", ans_array[i][0], ans_array[i][1])
