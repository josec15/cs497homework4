# Question 3
# K Largest Elements of a Max Heap

# Given a max heap as an array, implement List<Integer>peekTopK(int[] arr, int k)
# to find the top k elements. Do not modify the heap or copy entire heap to a different data structure.

from heapq import *


def findKLargestElements(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    return min_heap

nums = [15, 13, 12, 10, 8, 9]
k = 5
print(findKLargestElements(nums, k))