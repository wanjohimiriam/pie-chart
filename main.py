from tkinter import *
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt

# defining activities
activities= ["python", 'java', 'PHP', 'Web', 'Database']

#portion covered by each label
slices=[3,7,8,9,16]

#color for each label
colors=['r', 'y', 'g', 'b', 'c']

#plotting the pychart
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=TRUE, explode=(0,0,0.1,0,0), radius=1.2, autopct='%1.1f%%')

#plotting legends
plt.legend()

#showing the plot
plt.show()