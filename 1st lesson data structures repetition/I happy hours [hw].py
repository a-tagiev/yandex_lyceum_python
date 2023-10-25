hours = [i for i in input().split()]
mins = [i for i in input().split()]
s_h = 0
s_m = 0
ans = []
for i in hours:
    if len(i) == 1:
        s_h = int(i)
        i_f = "0" + i
    else:
        s_h = int(i) // 10 + int(i) % 10
        i_f = i
    for j in mins:
        if len(j) == 1:
            s_m = int(j)
            j_f = "0" + j
        else:
            s_m = int(j) // 10 + int(j) % 10
            j_f = j
        if s_m != s_h:
            ans.append(f"{i_f}:{j_f}")

print(*sorted(ans), sep="\n")
