def gcd(lst):
    a=lst[0]
    b=lst[1]
    while(b!=0):
        t=a
        a=b
        b=t%b
    return a

n=input("Enter the 2 numbers \n").split()
lst=[]
for num in n:
    lst.append(int(num))
print(f"The GCD of {lst[0]} and {lst[1]} is",gcd(lst))