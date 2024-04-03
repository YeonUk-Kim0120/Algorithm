num = 0
while True:
    isDead = False
    num += 1
    PW, RW = map(int,input().split())
    if PW == 0 and RW == 0:
        break
    while True:
        command, N = input().split()
        if command == "#" and N == "0":
            break
        if command == "F":
            RW += int(N)
        else:
            RW -= int(N)
            if RW <= 0:
                isDead = True
            
    if isDead:
        print(num, "RIP")
    elif 0.5*PW < RW < PW*2:
        print(num, ":-)")
    else:
        print(num, ":-(")