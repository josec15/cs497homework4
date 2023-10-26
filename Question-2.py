# Question 2
# Find K Closest Elements

# Given a sorted integer array arr, two integers k and x, 
# return the k closest integers to x in the array.
# The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a <  b

def findClosestElements(arr, k, x):
    leftptr = 0
    rightptr = len(arr) - k

    while leftptr < rightptr:
        mid = (leftptr + rightptr) // 2
        if x - arr[mid] > arr[mid + k] - x:
            leftptr = mid + 1
        else:
            rightptr = mid
    return arr[leftptr:leftptr + k]

arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(findClosestElements(arr, k, x))
