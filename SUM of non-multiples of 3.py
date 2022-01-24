sum = 0
sum = int(sum)
n = 100
while (sum <= n):
    x = input("Enter number:")
    x = int(x)
    if (x%3 == 0):
        continue
    sum = sum + x

sum = str(sum)
print('sum'+sum)