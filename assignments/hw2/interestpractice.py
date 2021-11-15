def main():
    # print the purpose of the program: calculate the value of an investment after 10 years
    print ("This program calculates the value of an investment after 10 years")
    # input the starting principal in the account
    principal = eval(input("input the starting principal in the account"))
    # input the interest rate
    apr = eval(input("input the interest rate"))
    # loop through 10 times
    for i in range (10):
        principal = principal * (1 + apr)  # calculate the principal after every year
    # principal * (1 + interest rate (apr))
    print("final account balance is: $", round(principal, 2))  # print the final account balance


if __name__ == "__main__":
    main()
