n = int(input("Hình vuông n x n?"))
for x in range(n):
    for y in range(n):
        print((x+1)*(y+1), end = " ")
    print()