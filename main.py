def myfunction(num):
    length = len(str(num))
    sum = 0
    for n in range(length):
        sum = sum + int(str(num)[n])
    return num+sum
print(myfunction(123))