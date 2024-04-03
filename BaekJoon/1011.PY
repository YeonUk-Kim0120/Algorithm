#failed
TC = int(input())
for i in range(TC):
    x, y = map(int,input().split())
    total = y-x
    half = (total)//2
    start = 0
    cnt = 0
    while start < half:
        cnt += 1
        start = start + cnt
        
    if cnt < 2:
        if (total - start) > (cnt*(cnt+1))//2 :
            cnt = cnt + cnt
        else:
            cnt = cnt+cnt-1
    else:
        if (total - start) > (cnt*(cnt-1))//2 :
            cnt = cnt + cnt
        else:
            cnt = cnt+cnt-1
    print(cnt)

