n=int(input('Please enter a number of which you would like to know the number of digits.\n'))
x=n
sum=2
while x//10>=10:
    x=x//10
    sum=sum+1
print('The number of digits in',n,'is',sum)