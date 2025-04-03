## Exercise 0:
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print(len(scores))

## Exercise 1:
print("The number of 3s in the list:", scores.count(3))

## Exercise 2:
print("The maximum score in the list is:", max(scores))

## Exercise 3:
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]

common_elements = []

for item in list_1:
    if item in list_2:
        common_elements.append(item)

print("Common elements:", common_elements)

## Exercise 4:
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]

positive_numbers = []
for item in all_numbers:
    if item in all_numbers > 0:
        positive_numbers.append(item)
print("possitive numbers are:", positive_numbers)
