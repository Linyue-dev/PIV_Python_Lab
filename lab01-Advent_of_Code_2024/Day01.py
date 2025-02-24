# initial 2 empties list
leftLines = []
rightLines = []

# Open the file 'Day-01.txt' in read mode
fh = open('Data/day-01', 'r')
#print(file.read())

# separate 2 lines for file
for line in map(str.rstrip,fh):
    left,right = line.split()
    # convert to int
    leftLines.append(int(left))
    rightLines.append(int(right))

fh.close()
# sorting lists
leftLines.sort()
rightLines.sort()


# print(leftLines)
# print(rightLines)

def totalGap(leftLines,rightLines):
    gap = 0
    for i in range(len(rightLines)):
        gap += rightLines[i] - leftLines[i]
    print(gap)

totalGap(leftLines,rightLines)