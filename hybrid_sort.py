# Python implementation of the above approach

# Function to perform the insertion sort
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val


# The following two functions are used
# to perform quicksort on the array.

# Partition function for quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[high] = a[high], a[j]
    return j


# Function to call the partition function
# and perform quick sort on the array
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr


# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            # Optimised quicksort which works on
            # the smaller arrays first

            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1


# Driver code

a = [24, 97, 40, 67, 88, 85, 15,
     66, 53, 44, 26, 48, 16, 52,
     45, 23, 90, 18, 49, 80, 23]
hybrid_quick_sort(a, 0, 20)
print(a)
