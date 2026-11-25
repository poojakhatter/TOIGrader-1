#Check for Armstrong Number
n = int(input())
original = n
temp = n
digits = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
