with open('input.txt', 'r') as file:
    lines = file.readlines()

floor_count = 0

for code in lines:
    for char in code:
        if char == "(":
            floor_count += 1
        else:
            floor_count -= 1
print(floor_count)