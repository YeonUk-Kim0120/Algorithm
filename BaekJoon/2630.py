def isAllSame(n, p):
    pivot = p[0][0]
    for i in range(n):
        for j in range(n):
            if pivot != p[i][j]:
                return False
    return True

def getWBNum(n, p, cnt):
    if (len(p) == 0):
        return
    if isAllSame(n,p):
        cnt[p[0][0]] += 1
        print("cnt + 1",p[0][0])
    else:
        n = n//2
        getWBNum(n, p[:n][:n], cnt)
        getWBNum(n, p[:n][n:2*n],cnt)
        getWBNum(n, p[n:2*n][:n],cnt)
        getWBNum(n, p[n:2*n][n:2*n],cnt)

N = int(input())
P = []
WBCnt = [0, 0]
for i in range(N):
    P.append(list(map(int,input().split())))

getWBNum(N,P, WBCnt)
#print(P)1
print(WBCnt[0])
print(WBCnt[0])