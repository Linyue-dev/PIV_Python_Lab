class Range:
    def __init__(self, n):
        self.end = n
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        #  Check if the count has reached the end value.
        if self.count >= self.end:
            raise StopIteration
        # Get the current value before incrementing.
        t = self.count
        self.count += 1
        return t

print("=============================================2 loops==============================================")
# Create an instance of the custom Range class
x = Range(5)
for i in x:
    print(i)
for j in x:
    print(j)
print("=======================Create a new Range instance for the inner loop=============================")
# Iterate through x twice using nested loops
for i in x:
    for j in Range(5): # Create a new Range instance for the inner loop
        print(i, j)
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 2 0
# 2 1
# 2 2
# 2 3
# 2 4
# 3 0
# 3 1
# 3 2
# 3 3
# 3 4
# 4 0
# 4 1
# 4 2
# 4 3
# 4 4
print("=============================================nested loops=========================================")
for i in x:
    for j in x:
        print(i, j)

# 0 0
# 0 1
# 0 2
# 0 3
# 0 4