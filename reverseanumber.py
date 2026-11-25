#reverse anumber
reverse=0
n=int(input('Enter number'))
while n>0:
    digit=n%10
    reverse=reverse*10 + digit
    n=n//10
    print('reverse:', reverse)

print(reverse)
