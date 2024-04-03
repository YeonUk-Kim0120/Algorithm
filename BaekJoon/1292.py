A, B = map(int,input().split())
lst = []
number = 0
ans = 0

while len(lst)<= 1000:
    number += 1
    for i in range(number):
        lst.append(number)

for i in range(A-1,B):
    ans = ans + lst[i]
print(ans)