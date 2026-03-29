# Simple Graph Plotting using Matplotlib

#  import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.plot(x, y)
# plt.title("DemoGraph") 
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8') # A in-built style

# Data for Pie Chart
labels = ['Python', 'SQL', 'ML', 'Design']
sizes = [40, 30, 20, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Setup Figure (2 rows, 3 columns for more variety)
fig = plt.subplots_adjust(hspace=0.4)
fig = plt.figure(figsize=(15, 10))
fig.suptitle('Matplotlib Graphs', fontsize=18, fontweight='bold')

#  Pie Chart 
ax2 = fig.add_subplot(2, 3, 1) # Position 1 in a 2x3 grid 
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0.1, 0, 0, 0))
ax2.set_title('Pie Chart (plt.pie)')

# Bar Graph 
ax3 = fig.add_subplot(2, 3, 2) # Position 2 in a 2x3 grid
ax3.bar(['A', 'B', 'C'], [10, 24, 15], color='teal')
ax3.set_title('Bar Graph (plt.bar)')

# Line Graph 
ax4 = fig.add_subplot(2, 3, 3) # .add_subplot(nrows, ncols, index) 
ax4.plot(np.linspace(0, 10, 20), np.cos(np.linspace(0, 10, 20)),  color='blue', marker='o', linestyle='--', label='Growth')
ax4.set_title('Line Plot (plt.plot)')
ax4.grid(True, linestyle=':')
ax4.legend()

# Scatter Plot 
ax5 = fig.add_subplot(2, 3, 4)
ax5.scatter(np.random.rand(30), np.random.rand(30), s=100, c='purple', alpha=0.6)
ax5.set_title('Scatter (plt.scatter)')

# Histogram 
ax6 = fig.add_subplot(2, 3, 5)
ax6.hist(np.random.normal(0, 1, 500), bins=20, color='darkslategrey', alpha=0.8)
ax6.set_title('Histogram (plt.hist)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent overlap with the title
plt.show() # Displays the graph in a new window

