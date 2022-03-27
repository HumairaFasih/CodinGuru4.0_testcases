import sys
with open('output00.txt', 'w') as output_file:
    sys.stdout = output_file
    T = int(input())
    ans_array = []

    for testcase in range(T):
        input()
        s = list(map(int, input().split()))
        k = 0
        while s[0] <= max(s[1:]):
            s[1+s[1:].index(max(s))] -= 1
            s[0] += 1
            k += 1
        ans_array.append(k)
    for i in range(len(ans_array)):
        print(f"Case #{i + 1}:", ans_array[i])
