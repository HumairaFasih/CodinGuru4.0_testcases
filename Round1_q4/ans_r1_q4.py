import sys
with open('output02.txt', 'w') as output_file:
    sys.stdout = output_file
    
    T = int(input())
    print(T)
    ans_array = []

    for testcase in range(T):
        input()
        r, s = 0, 0
        for i in sorted(map(int, input().split())):
            if s <= i:
                s += i
                r += 1
        ans_array.append(r)
    for i in range(len(ans_array)):
        print(f"Case #{i + 1}:", ans_array[i])
    for i in range(len(ans_array)):
        print(f"Case #{i + 1}:", ans_array[i])
