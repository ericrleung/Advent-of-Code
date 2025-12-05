with open('input.txt', 'r') as file:
    lines = file.readlines()

ans = set()
santacur = (0, 0)
robocur = (0, 0)
ans.add(santacur)

for line in lines:
    for i in range(len(line)):
        if i % 2 == 0:
            if line[i] == "^":
                santacur = (santacur[0], santacur[1] + 1)
            elif line[i] == "v":
                santacur = (santacur[0], santacur[1] - 1)
            elif line[i] == "<":
                santacur = (santacur[0] - 1, santacur[1])
            else:
                santacur = (santacur[0] + 1, santacur[1])
            ans.add(santacur)
        else:
            if line[i] == "^":
                robocur = (robocur[0], robocur[1] + 1)
            elif line[i] == "v":
                robocur = (robocur[0], robocur[1] - 1)
            elif line[i] == "<":
                robocur = (robocur[0] - 1, robocur[1])
            else:
                robocur = (robocur[0] + 1, robocur[1])
        #print(robocur)
            ans.add(robocur)
print(len(ans))