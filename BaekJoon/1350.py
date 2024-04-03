TC = int(input())
lst = list(map(int,input().split()))
cluster = int(input())
total = 0
for i in lst:
    if i//cluster == (i/cluster):
        c_num = i//cluster
    else:
        c_num = i//cluster + 1
    total += (c_num*cluster)
print(total)
