#Input any 10 numbers find out no of even numbers and no of odd numbers
numbers = []
n = int(input("Enter number of elements: \t"))
for i in range(1, n + 1):
    allElements = int(input("Enter element:"))
    numbers.append(allElements)

even_lst = []
odd_lst = []

for j in numbers:
    if j % 2 == 0:
        even_lst.append(j)
    else:
        odd_lst.append(j)

print("Even numbers list \t", even_lst)
print("Odd numbers list \t", odd_lst)