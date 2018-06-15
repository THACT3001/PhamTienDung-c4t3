numbers = [1, 6, 8, 1, 2, 1, 5, 6]

so_lan = 0

n = int(input("Enter a number: "))

for i in numbers:
    if i == n:
        so_lan = so_lan + 1
print("So lan ", n, "xuat hien trong day la", so_lan, "lan")
