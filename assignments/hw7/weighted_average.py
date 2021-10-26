"""
Name: evie fleischman
weighted_average.py

Problem: This program finds the averages of students and then tells the user whether or not their weights equal to 100.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        split_one = line.split(":")
        split_nums = split_one[1].split(" ")
        total = 0
        for i in range(1, len(split_nums), 2):
            total += int(split_nums[i])
        if total < 100:
            outfile.write("Error: The weights are less than 100.")
        elif total > 100:
            outfile.write("Error: The weights are more than 100.")
        else:
            avg = 0
            for j in range(1, len(split_nums), 2):
                grades_times_weights = eval(split_nums[j]) * eval(split_nums[(j+1)])
                avg += grades_times_weights
            avg = avg/100
        outfile.write(str(split_one[0]) + "'s average: " + str(avg) + "\n")


def main():
    if __name__ == '__main__':
        weighted_average("grades.txt", "avg.txt")


main()
