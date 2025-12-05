with open('input.txt', 'r') as file:
    lines = file.readlines()

ans = set()
cur = (0, 0)
ans.add(cur)

for line in lines:
    for char in line:
        if char == "^":
            cur = (cur[0], cur[1] + 1)
        elif char == "v":
            cur = (cur[0], cur[1] - 1)
        elif char == "<":
            cur = (cur[0] - 1, cur[1])
        else:
            cur = (cur[0] + 1, cur[1])
        print(cur)
        ans.add(cur)
print(len(ans))