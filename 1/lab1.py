import numpy as np
import matplotlib.pyplot as plt

def shift(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result = arr

    n = len(arr)
    print(n)
    for i in range(num - 1, 0, -1):
        result[i] = arr[n - i -1]
    result[0] = arr[-1]
    return result

n = 100 #input("enter n: ")
m = 17 #input("enter m: ")
k = 7 #input("enter k: ")
A = 2 #input("A: ")
mm_method = np.zeros((int(n)))
print(n, m, k)

for i in range(n):
    A = np.mod(k*A,m)
    mm_method[i] = A

mm_method = np.divide(mm_method,np.amax(mm_method))
print(mm_method)

step = 10
intervals = np.arange(0, 1.1, 1/(step))
intervals_stat = np.zeros((step))
mm_method_unsorted = np.copy(mm_method)
mm_method = np.sort(mm_method)

interval_number = 0
print(intervals)
wtf_counter = 0
for counter in range(n):

    print(counter, interval_number, mm_method[counter], intervals[interval_number])
    if interval_number < step - 1:
        if mm_method[counter] >= intervals[interval_number + 1]:
            print("0")
            print("update", interval_number, mm_method[counter], ">",intervals[interval_number])

            #while (mm_method[counter] > intervals[interval_number]) and (interval_number < step - 1 ):
            interval_number += 1
            intervals_stat[interval_number] += 1
            continue
    else:
        intervals_stat[interval_number] += n - counter
        print("all done", mm_method[counter], interval_number)
        break

    if mm_method[counter] == intervals[interval_number]:
        print("1")
        intervals_stat[interval_number] += 0.5
        if interval_number > 0:
            intervals_stat[interval_number - 1] += 0.5

    elif (mm_method[counter] > intervals[interval_number]) and (mm_method[counter] < intervals[interval_number + 1]):
        intervals_stat[interval_number] += 1
        print("2")
    else:
        print("\n!!!!!!!!!! smth got wrong",  mm_method[counter], interval_number, intervals[interval_number])
        wtf_counter +=1
    # print(intervals[interval_number])
    #interval_number += 1

print(intervals_stat)
print(np.sum(intervals_stat) , wtf_counter,np.sum(intervals_stat)/n)

dict ={}


x_range = np.zeros((step))
for i in range(step):
    x_range[i] = (intervals[i] + intervals[i + 1])/2

print(x_range)
x_range_2 = np.arange(0.1, 1.1, 1/(step))
'''
plt.plot(x_range, intervals_stat, '|')
plt.grid(True)
plt.legend ( ("max with s", "max with disp") )
plt.show()
'''

#plt.hist(intervals_stat)
#plt.show()


x = x_range_2 #np.arange(len(x_range))
width = 0.08
fig, ax = plt.subplots(figsize=(15,5))
rects1 = ax.bar(x - width/2, intervals_stat, width, label='sepal width')
#rects2 = ax.bar(x + width/2, intervals_stat, width, label='petal width')

ax.set_ylabel('cm')
ax.set_xticks(x)
ax.legend()
#plt.show()

convergence_of_frequency = np.divide(intervals_stat, step)
expected_value = 1/n * (np.sum(mm_method))
dispersion = 1/n *np.sum((np.power(mm_method,2) - np.power(expected_value, 2)))
print("expected_value", expected_value, "dispersion", dispersion)

correlation_check_step = 10
#for i in range(len(mm_method_unsorted)):
#    correlation = np.sum()

shifted_array = shift(mm_method_unsorted, 10)
#print(mm_method_unsorted, "\n\n",shifted_array)
numerator = np.sum(mm_method_unsorted - expected_value) * np.sum(shifted_array - expected_value)
denominator = ( np.power(np.sum(mm_method_unsorted - expected_value), 2) * np.power(np.sum(shifted_array - expected_value),2))
#denominator = np.sqrt( np.power(np.sum(mm_method_unsorted - expected_value), 2) * np.power(np.sum(shifted_array - expected_value,2)))
correlation = np.divide(numerator,denominator)
print("correlation", correlation)