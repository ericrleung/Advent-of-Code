with open('input.txt', 'r') as file:
    lines = file.readlines()

floor_count = 0

for code in lines:
    for i in range(len(code)):
        if code[i] == "(":
            floor_count += 1
        else:
            floor_count -= 1
        if floor_count == -1:
            print(i + 1)
            break
print(floor_count)