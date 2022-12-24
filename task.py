array = [input() for i in range(5)]
res = []

for i in array:
    if len(i) < 4 : res.append(i)

print(res)    