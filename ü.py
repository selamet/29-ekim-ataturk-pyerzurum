str = ""
for i in range(15):
    for j in range(15):
        if ((j == 0 or j == 1 or j == 2 or j == 12 or j == 13 or j == 14) and (i >= 1 and i != 3)) or (j>0 and (i == 14 or i == 15)):
            str = str + "*"

        else:
            str = str + " "
    str = str + "\n"
print(str)
