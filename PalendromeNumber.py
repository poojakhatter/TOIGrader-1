#Check number is palendrome or not
#reverse anumber
reverse=0
n=int(input('Enter number'))
original=n

while n>0:
    digit=n%10
    reverse=reverse*10 + digit
    n=n//10
    print('reverse:', reverse)

if original==reverse:
    print('No is Palendrome')
else:
    print('No is not Palendrome')
    
