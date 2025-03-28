# 6. Multiplication Table

print("write any number and I will  give you multiplication table for it")
chosen_number = int(input())
something = 1
while something <= 10 :
    print(f"{chosen_number} * {something} = {chosen_number * something}")
    something += 1