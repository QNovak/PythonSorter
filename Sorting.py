numbers = [67,45,2,13,1,998]
output = []

while numbers:
    smallest = min(numbers)
    index = numbers.index(smallest)
    output.append(numbers.pop(index))

print(output)

numbers_2 = [89,23,33,45,10,12,45,45,45]
output = []

while numbers_2:
    smallest = min(numbers_2)
    index = numbers_2.index(smallest)
    output.append(numbers_2.pop(index))

print(output)

