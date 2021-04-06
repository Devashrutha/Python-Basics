def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n< 0:
        return "Incorrect Input"
    else:
        return n*factorial(n-1)
k=int(input("Enter the number \n"))
print("The factorial of",k,"is:",factorial(k))