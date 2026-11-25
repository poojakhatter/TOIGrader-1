#Sum of digits

total=0
n=int(input('Enter number'))
while n>0:
    print(n)
    digit=n%10  #n % 10 extracts the last digit.
    print('digit',digit)
    total=total+digit
    print('total',total)
    n=n//10   #remove the last digit
    print('n',n)

print(total)
    
