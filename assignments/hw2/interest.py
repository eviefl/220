"""
Name: evie fleischman
interest.py

Problem:
This program solves the problem of being able to find the monthly interest for an account.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    import math
    interest_rate = (eval(input("Enter the annual interest rate of the account: ")))
    net = eval(input("Enter the net balance of the account: "))
    billing = (eval(input("Enter the number of days in the billing cycle: ")))
    net_amount = net * billing
    payment_received = (eval(input("Enter the net payment made to account: ")))
    days = (eval(input("Enter the number of days into the billing cycle payment was made: ")))
    bill_received = billing - days
    end_of_cycle = payment_received * bill_received
    amount = net_amount - end_of_cycle
    average_daily_balance = amount / billing
    annual_interest = average_daily_balance * interest_rate
    monthly_interest_rate = interest_rate / 12
    monthly_interest_rate = monthly_interest_rate / 100
    monthly_interest = average_daily_balance * monthly_interest_rate
    print("Monthly Interest: $", monthly_interest)


main()
