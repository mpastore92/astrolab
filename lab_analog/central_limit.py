# Marta Pastore
# Radio Astronomy Lab
# February 10, 2014



# Central Limit Theorem Code

from matplotlib import pyplot as plt
import numpy
import numpy.random

N = 1000
sample_size = 10
averages = []
count = 0

while count < N:
    numbers = numpy.random.randint(1,50,sample_size)
    average = numpy.average(numbers)
    averages.append(average)
    count = count + 1

count,bins,patches = plt.hist(averages,50,normed=1,facecolor='g')
plt.show()
