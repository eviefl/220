"""
Name: evie fleischman
sales_force.py
Problem: This program encapsulates data for a sales person.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                split_line = line.split(", ")
                person = SalesPerson(int(split_line[0]), split_line[1])
                sales = split_line[2].split()

                for num in sales:
                    person.enter_sale(float(num))
                self.sales_people.append(person)

    def quota_report(self, quota):

        output_list = []
        for person in self.sales_people:
            employee_id = person.get_id()
            name = person.get_name()
            total_sales = person.total_sales()
            quota_bool = person.met_quota(quota)

            person_list = [employee_id, name, total_sales, quota_bool]
            output_list.append(person_list)
        return output_list

    def top_seller(self):
        sales = self.sales_people
        top_seller = [sales[0]]
        for person in range(1, len(sales)):
            if sales[person].total_sales() > top_seller[0].total_sales():
                top_seller = [sales[person]]
            elif sales[person].total_sales() == top_seller[0].total_sales():
                top_seller.append(sales[person])
        return top_seller

    def individual_sales(self, employee_id):
        people = self.sales_people

        for person in people:
            if person.get_id() == employee_id:
                return person
        return None
