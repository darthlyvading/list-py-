lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    lst.append(elem)


total = 0
for elem in lst:
    if elem>0:
        total+=elem

print("sum of all positive numbers is ",total)