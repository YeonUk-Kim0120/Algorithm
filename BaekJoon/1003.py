lst = [[1,0],[0,1]] # f(0)과 f(1)일때의 [0의개수, 1의 개수]
for i in range(2, 41):
    n_nums = [lst[i-1][0]+ lst[i-2][0], lst[i-1][1]+ lst[i-2][1]]
    lst.append(n_nums)
    

T = int(input())
for i in range(T):
    N = int(input())
    print(lst[N][0], lst[N][1])