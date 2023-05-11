import time
import random

ARRAY_SIZE = 1000 # can be changed to something smaller for testing,... (like 10)

# Complete the two functions below that sorts the array of integers
# using bubble sort and quick sort algorithms respectively
# Reference material:
# - https://youtu.be/RGuJga2Gl_k?t=111
# - https://www.toptal.com/developers/sorting-algorithms
# - https://www.geeksforgeeks.org/quick-sort/
# - Google bubble sort or quick sort for more information this are
#   very popular sorting algorithms. Dont bother with the ChatGPT
#   the algorithms are well explained online you just need to understand them
#   and implement them in python. We are doing benchmark so we can see that
#   we can do the same thing using diferent algoriths and archive a big
#   performance increase.
#
# You can also try to implement other sorting algorithms and beat these two...

def bubble_sort(arr):
    sorted_arr = arr.copy()
    # TODO: Sort arr using bubble sort
    return sorted_arr

def quick_sort(arr):
    sorted_arr = []
    # TODO: Sort arr using quick sort
    return sorted_arr


#### DO NOT CHANGE CODE BELOW THIS LINE ####
# Benchmarking code
array = random.sample(range(1, 100000), ARRAY_SIZE)

# Benchmarking Bubble Sort
start_time = time.time()
sorted_array = bubble_sort(array)
end_time = time.time()
if(ARRAY_SIZE < 20):
    print("Original Array:", array)
    print("BubbleSort Sorted Array:", sorted_array)
print(f"Bubble Sort Execution Time: {((end_time - start_time) * 1000):.2f} milliseconds")

# Benchmarking Quicksort
start_time = time.time()
sorted_array = quick_sort(array)
end_time = time.time()
if(ARRAY_SIZE < 20):
    print("Original Array:", array)
    print("QuickSort Sorted Array:", sorted_array)
print(f"Quick Sort Execution Time: {((end_time - start_time) * 1000):.2f} milliseconds")
