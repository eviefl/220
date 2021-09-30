"""
Name: evie fleischman
traffic.py

Problem:This program solves the problem of DOT needing to analyze traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    acc_veh_per_road = 0
    num_of_roads = eval(input("How many roads were surveyed? "))
    for i in range(num_of_roads):
        num_of_days = eval(input("How many days was road " + str(i + 1) + " traveled? "))
        acc_cars = 0
        for j in range(num_of_days):
            num_of_cars = eval(input("How many cars traveled on day " + str(j + 1) + " ? "))
            acc_cars += num_of_cars
        avg_road = acc_cars / num_of_days
        print("Road " + str(i) + " average vehicles per day: " + str(avg_road))
        acc_veh_per_road += acc_cars
    print("Total number of vehicles traveled on all roads: " + str(acc_veh_per_road))
    avg = acc_veh_per_road / num_of_roads
    round(avg, 2)
    print("Average number of vehicles per road: " + str(avg))


main()
