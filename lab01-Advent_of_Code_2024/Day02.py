# initialize a two-dimensional list
reports = []

# create function for count of safe in reports
def count_safe_reports():
    count_safe = 0
    with open ('Data/day-02','r') as file:
        for line in file:
            # Convert the line into a list of integers
            report = list(map(int, line.split()))
            reports.append(report)
            if is_safe(report):
                count_safe += 1
    return count_safe

# create function for verified safe list
def is_safe(report):
    # verified the levels are either all increasing or all decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    # verified any two adjacent levels differ by at least one and at most three
    adjacent_differ = all( 1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

    return (increasing or decreasing)  and adjacent_differ

# Output the number of safe reports
print("Number of safe reports:", count_safe_reports())
