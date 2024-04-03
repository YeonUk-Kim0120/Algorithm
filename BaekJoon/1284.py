while True:
    width = 0
    number = input()
    if number == "0":
        break
    for i in number:
        if int(i) == 1:
            width += 2
        elif int(i) == 0:
            width += 4
        else:
            width += 3
    width += len(number) + 1
    print(width)