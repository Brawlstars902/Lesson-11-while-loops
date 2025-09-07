x=int(input('Please enter a number of which you would like to find the sum of all of the numbers less than and equal to it.\n'))
sum=0
i=1
while i<=x:
    sum=sum+i
    i=i+1
print('The sum of all the numbers less than and equal to',x,'is',sum)