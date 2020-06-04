# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


            # start at current index, loop through rest of the array to the right, if a smaller value is found, store that index location as smallest.
        j=i
        temp = arr[cur_index]
        while j < len(arr):
            if (arr[j] < arr[smallest_index] ):
                smallest_index = j
            j+=1
        # swap the smallest index with current index in the array
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
        # current index moves to the right and contines loop
                


            
            


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

# Swap Count to track swaps during for loop, if no swaps occur, array is ordered
    swapCount = 1
# When at the end of the list, if swap count is 0, you are done. Else reset swap count to 0 and start over
    while swapCount > 0:
        swapCount = 0
        for i in range(0, len(arr)-1):
            # if( arr[i+1] ):
# Start with first index, compare with next index in list, if greater than next index, switch the two indexes
            if( arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
# Change swap count to 1
                swapCount = 1
# Move to next index and restart the loop


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

# ourList = [2, 5, 4, 3, 6, 7] 
# print(selection_sort(ourList))
# print(bubble_sort(ourList))
