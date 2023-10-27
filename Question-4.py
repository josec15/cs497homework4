# Question 4
# Shortest Subarray with Sum at least K

# Given an integer array nums and an integer k, return the length of the shortest non-empty
# subarray of nums with a sum of at least k. If there is no such subarray, return -1.
import sys

def smallestSubarraySumK(arr,  k):
    result = sys.maxsize
    for i in range(0, len(arr)): 
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if (sum_ == k): 
                result = min(result, (j - i + 1))
    return result

arr = [2, -1, 2]
k = 3
 
result = smallestSubarraySumK(arr, k)
if (result == sys.maxsize):
    print(-1)
else:
    print(result)