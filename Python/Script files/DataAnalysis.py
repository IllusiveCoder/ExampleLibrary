# Example: Data analysis - Calculating mean and standard deviation

'''
Explanation:
    This program calculates the mean and standard deviation of a list of data.
    The mean is calculated by summing all data points and dividing by the number of points.
    The standard deviation is calculated using the formula, involving the mean and squared differences from the mean.
'''

# Sample data
data = [12, 15, 18, 22, 25, 30]

# Calculate mean
mean = sum(data) / len(data)

# Calculate standard deviation
std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5

# Output the results
print("Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
