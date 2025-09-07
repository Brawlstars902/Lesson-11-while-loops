x=int(input('Please enter a number to see if it is an armstrong number or not.\n'))
sum=0
temp=x
while temp>0:
    digit=temp % 10
    sum+=digit**3
    temp//=10
if x==sum:
    print(x,'is an armstrong number.')
else:
    print(x,'is not an armstrong number.')