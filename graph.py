from cProfile import label
import matplotlib.pyplot as plt
 
# problem size
x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]
values = range(len(x))

# normal time
#y1 = [0, 1.29, 2.95, 13.96, 33.03, 54.81, 137.25, 263.36, 362.61, 522.74, 1005.32, 1658.18, 2201.66, 3293.03, 4137.07]
#y2 = [0, 0.99, 4.02, 18.93, 44.79, 76.30, 163.20, 278.88, 433.07, 610.48, 1260.16, 2126.54, 2482.99, 3677.34, 4517.95]

y1 = [14364, 14376, 14532, 14944, 15880, 17256, 20404, 24992, 31024, 38568, 57144, 80812, 108704, 145348, 171264]
y2 = [14792, 14792, 14680, 14860, 14860, 14876, 14924, 15036, 14964, 15180, 15068, 15068, 15296, 15280, 15408]



# plotting the points
plt.plot(values, y1, label= 'Basic')
plt.plot(values, y2, label = 'Efficient')



# naming the x axis
plt.xlabel('PROBLEM SIZE (M+N)')
# naming the y axis
plt.ylabel('MEMORY USAGE (KB)')

 
# giving a title to my graph
plt.title('Memory Usage vs Problem Size')
plt.xticks(values,x)

plt.legend()
 
# function to show the plot
plt.show()