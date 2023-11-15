# Example: Data Visualization - Plotting a simple graph

'''
Explanation:
    This program uses the matplotlib library to plot a simple graph of temperature variation over a few days.
    The plot function is used to specify the data points, and various parameters control the appearance of the graph.
    Labels and a title are added to make the graph informative.
    These additional Python examples cover data analysis, GUI application development, and data visualization. Feel free to explore and modify these examples according to your needs!'''

import matplotlib.pyplot as plt

# Sample data
days = [1, 2, 3, 4, 5]
temperature = [25, 28, 24, 30, 22]

# Plotting the graph
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation')

# Display the graph
plt.show()
