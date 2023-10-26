#Question 1
# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order. Your algorithm's time complexity
# must be better than O(nlogn), where n is the array's size.

from ast import List

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n, c in count.items():
        freq[c].append(n)
        
    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))

