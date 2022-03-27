import sys
with open('Sample_output_q1.txt', 'w') as output_file:
    sys.stdout = output_file
    T = int(input())
    ans_array = []

    for testcase in range(T):
        n = int(input())
        h = list(map(int, input().split()))
        S = sorted([(h[i], i) for i in range(n)])
        A = [S[i][1] for i in range(n)]
        swp = [(0, 0)]
        found_possible = False
        for i in range(n-1):
            if S[i][0] == S[i+1][0]:
                swp.append((i, i+1))
                if len(swp) == 3:
                    found_possible = True
                    ans_array.append("POSSIBLE")
                    for i, j in swp:
                        A[i], A[j] = A[j], A[i]
                        repair_schedule = list(repr(a+1) for a in A)
                        ans_array.append(repair_schedule) 
        if found_possible == False:
            ans_array.append("IMPOSSIBLE")

    count = 0
    for i in range(len(ans_array)):
        if ans_array[i] == "IMPOSSIBLE" or ans_array[i] == "POSSIBLE":
            count += 1
            print(f"Case #{count}:", ans_array[i])
        else:
            print(" ".join(ans_array[i]))
