#function created to carry out the factorial operation
def factorial(x):
    if x == 1:
        return 1
#factorial of 0 is 1 hence the if statement is necessary as python would return this value as 0.
    elif x == 0:
        return 1
    else:#factorial function using a recursive formula
        return (x * factorial(x - 1))

#function used to implement the calculation of the combination.
def combination(n, k):
    if k == 0:
        return 1
    else:
        B = factorial(n) / (factorial(k) * factorial(n - k))
    return ((B)*(Cx**(n-k))*(Cy**k))

#function created to calculate the coefficient of all terms.
def final_coefficients(n,k):
    k=0
#for loop used to iterate k value in order to get all values of k from 0 up to n.
    for k in range(k,n+1):
        k+1
        B = factorial(n)/(factorial(k)*factorial(n-k))
        RHS = (B * Cx **(n-k) * Cy**k)
        print("The final coefficients are", RHS)

choice = " "
#A while loop where the user is prompted to enter their chosen option.
while choice != "":
    choice = input(
        "Enter A,B,C or D\nOption A terminates the program\nOption B is Capture the Cx,Cy and exponent n\nOption C Calculates and display the final coefficients\nOption D is to calculate and display the Kth term")
#option A is included which allows the user to exit the program.
    if choice == "A":
        print("You have terminated the program.")
        break
        quit()
#option B is included and it allows the user to input values for the coefficient of the x term Cx and the coefficient of the y term Cy and the exponent n.
    elif choice == "B":
        Cx = float(input("enter the coefficient of x="))
        Cy = float(input("enter the coefficient of y="))
        n = float(input("enter the value for the binomial exponent="))
        print("The value for the coefficient of x is,", Cx, ",the value of the coefficient of y is", Cy,
              ",the value of the binomial exponent is", n, ".")
#option C prompts the user to put in Cx,Cy and n before calculating the coefficients of all terms. It uses the function coefficient2 created earlier.
    elif choice == "C":
        Cx = float(input("enter the coefficient of x="))
        Cy = float(input("enter the coefficient of y="))
        n = eval(input('Please input the binomial exponent: '))  # variable n will be the users input
        k = n
        print(final_coefficients(n,k))
#option D will calculate the Kth coefficient. The kth term for any binomial expansion can be calculated using this.
    elif choice == "D":
        Cx = float(input("enter the coefficient of x="))
        Cy = float(input("enter the coefficient of y="))
        n = float(input("enter the value for the binomial exponent="))
        k = n
        print("The final coefficient is",combination(n,k))
#If A,B,C or D is not entered then the programme will prompt the user to reenter an option on the list.
    else:
        print("Enter an option on the list.")