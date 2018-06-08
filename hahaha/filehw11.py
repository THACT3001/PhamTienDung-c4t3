sizes = [5, 7, 300, 90, 24, 50, 75]

print("Hello my name is Dung and these are my ship sizes: ", *sizes, end = " ")
print()

print("Now my biggest sheep has size", max(sizes),"let's shear it")
print()

sizes[sizes.index(max(sizes))] = 8
print("After shearing, here is my flock:", *sizes, end = " ")
print()

sizes = [size + 50 for size in sizes]
print("One month has passed, now here is my flock:", *sizes, end = " ")
print()

month = int(input("Month? "))
for i in range(month):
    print("MONTH", i + 1, ":")
    sizes = [size + 50 for size in sizes]
    print("One month has passed, now here is my flock:", *sizes, end=" ")
    print()
    print("Now my biggest sheep has size", max(sizes), "let's shear it")
    print()
    sizes[sizes.index(max(sizes))] = 8
    print("After shearing, here is my flock:", *sizes, end=" ")
    print()
print("The total size of my flock is: ", sum(sizes))
print("I would get", sum(sizes), "* 2$ =", sum(sizes) * 2, "$ if I sell all of my sheeps")