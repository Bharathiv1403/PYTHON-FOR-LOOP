num=6
latter="B"
for i in range(num):
    print((latter*i).rjust(num-1)+latter+(latter*i).ljust(num-1))
