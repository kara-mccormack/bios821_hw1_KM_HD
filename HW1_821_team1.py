# Create function to get data
def get_data(path):
    """Python Function to read in .txt file"""
    with open(path, "r") as file:
        full_list = []
        for line in file:
            line = [int(i) for i in line.split()]
            full_list.append(line)
    return full_list
    # this returns a list


# To use the get_data function make sure you pull a file from your directory
# test = get_data("/Users/hannahdamico/Desktop/W22/BIOSTAT 821/example.txt")
# test = get_data("/Users/maireaddillon/biostat821/example.txt")

import math

# Create function to analyze data
def analyze_data(list, command):
    """ "Python function to analyze integers"""
    n1 = len(list[0])
    avg1 = sum(list[0]) / n1

    n2 = len(list[1])
    avg2 = sum(list[1]) / n2

    if command == "average":
        # this computes the average of a list of integers
        average = sum(list[0] + list[1]) / (n1 + n2)
        return average
    elif command == "standard deviation":
        # this computes the std. deviation of list
        average = sum(list[0] + list[1]) / (n1 + n2)
        # for loop cycles through list, computes std.dev
        numerator = 0
        for i in list[0] + list[1]:
            numerator += (i - average) ** 2
        std_dev = math.sqrt(numerator / (n1 + n2))
        return std_dev
    elif command == "covariance":
        # first line in list
        multiplied = 0
        for (x, y) in zip(list[0], list[1]):
            multiplied += (x - avg1) * (y - avg2)
        # final covariance computation
        cov = multiplied / n1
        return cov
    elif command == "correlation":
        # first line in list
        multiplied = 0
        for (x, y) in zip(list[0], list[1]):
            multiplied += (x - avg1) * (y - avg2)
        # final covariance computation
        cov = multiplied / n1

        numerator3 = 0
        numerator4 = 0
        # variance list 1
        for i in list[0]:
            numerator3 += (i - avg1) ** 2
        var1 = numerator3 / n1
        # variance list 2
        for j in list[1]:
            numerator4 += (j - avg2) ** 2
        var2 = numerator4 / n2

        # correlation
        corr = cov / math.sqrt(var1 * var2)
        return corr


# Run function for each command
# print(analyze_data(test, "average"))
# print(analyze_data(test, "standard deviation"))
# print(analyze_data(test, "covariance"))
# print(analyze_data(test, "correlation"))
