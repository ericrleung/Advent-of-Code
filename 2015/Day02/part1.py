with open('input.txt', 'r') as file:
    lines = file.readlines()

ans = 0

for line in lines:
    d = line.strip().split("x")
    d = [int(x) for x in d]
    ans += int(2 * d[0] * d[1] + 2 * d[1] * d[2] + 2 * d[0] * d[2] + d[0] * d[1] * d[2] / max(d[0], d[1], d[2]))
print(ans)