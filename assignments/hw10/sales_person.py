"""
Name: evie fleischman
sales_person.py
Problem: This program encapsulates data for a sales person
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""


class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        employee_id = self.employee_id
        return employee_id

    def get_name(self):
        name = self.name
        return name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total_sales = sum(self.sales)
        return total_sales

    def get_sales(self):
        sales = self.sales
        return sales

    def met_quota(self, quota):
        total_sales = self.total_sales()
        met_quota = bool(total_sales >= quota)
        return met_quota

    def compare_to(self, other):
        person_total = self.total_sales()
        other_total = other.total_sales()
        if other_total > person_total:
            comparison_num = -1
        elif person_total > other_total:
            comparison_num = 1
        else:
            comparison_num = 0
        return comparison_num

    def __str__(self):

        employee_id = self.employee_id
        name = self.name
        total_sales = self.total_sales()
        employee_information = ("{0}-{1}: {2}".format(employee_id, name, total_sales))
        return employee_information
