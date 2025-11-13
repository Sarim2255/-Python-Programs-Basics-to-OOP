list = [3,5,-1,0,9]
min = list[0]
max = list[0]

for i in list:
    if i < min:
        min = i
    elif i > max:
        max = i

print("Maximum: ", max)                # 9
print("Minimum: ",min)                 # -1