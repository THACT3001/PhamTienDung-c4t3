from random import *
list = ["Spring", "Summer", "Autumn", "Winter", "Jellyfish"]
bien_random = randrange(list)
list_rỗng = [ ]
for i in list[bien_random]:
    x = randrange(0, len(list[bien_random]))
    list_rỗng.insert(x, i)
print(list_rỗng)
doan = input("Đoán đi")
if doan == bien_random:
    print("Hura")
else:
    print("Sai rồi")


