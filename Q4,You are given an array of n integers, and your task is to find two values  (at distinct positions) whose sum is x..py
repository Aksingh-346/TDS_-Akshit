#Python
while True:
    lst = []
    switch = "ON"
    inpN = int(input("Enter the array size: "))
    inpX = int(input("Enter the target sum: "))
    for i in range(inpN):
        inpA = int(input("Enter the nos.: "))
        lst.append(inpA)
    for a in lst:
        for b in lst:
            if a+b == inpX:
                print((lst.index(a))+1,(lst.index(b))+1)
                switch = "OFF"
            else:
                continue
    if switch == "ON":
        print("IMPOSSIBLE")
