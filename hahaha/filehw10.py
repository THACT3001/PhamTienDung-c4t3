
clothes = ["T-Shirt", "Sweater"]

letter = input("Welcome to our shop, what do you want (C, R, U, D)?")

if letter != "c" and letter != "r" and letter != "u" and letter != "d":
    print("Invalid letter. Please retry.")
elif letter == "c":
    item = input("Enter new item: ")
    clothes.append(item)
    print("Our items: ", *clothes, end = " ")
elif choice == "r":
    print("Our items:", *clothes, end = " ")
elif choice == "u":
    vi_tri = int(input("Enter new position: "))
    do_moi = input("Enter new item: ")
    clothes[position - 1] = do_moi
    print("Our items: ", *clothes, end = " ")
else:
    vi_tri_xoa = int(input("Enter position: "))
    clothes.pop(vi_tri_xoa -1)
    print("Our items: ", *clothes, end = " ")

