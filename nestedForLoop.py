# prints times table from 1 - 10 in nested for loop

for i in range(1, 21):
    for j in range(1, 21):
        result = i * j
        print(f"{i} x {j} = {result}")
