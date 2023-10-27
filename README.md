# CS497 Homework 4

## Question 1
Begin by creating a mashmap to count the occurences of each value.  
Create a frequency array where the index is the frequency of the value in the nums list  
and the value is the number that corresponds with the frequency. The size of the array is proportional  
to the size of the nums list since the number's frequency is equal to the numbers in the list.  
The first for loop will count how many times n(each value in nums) occurs in the list.  
The second for loop will append the value to the index of frequency which represents the number  
of times the value in nums lists occurs. Once the entire nums list has been traversed, we will create  
a result array and traverse the frequency array backwards starting from the last index. We will append the i   index of the frequency to the result array until the size of the array matches the value k.  
Once that condition is satisfied we can return the result. Time complexity = O(n), because we traverse the  
array n times.

## Question 2
First initialize a left and right pointer that will be used to do a binary search from the target value.  
While the pointers are not pointing to the same value, we calculate the mid point and if the target value minus the mid point value of the array is greater than the mid point value plus k minus the target value then we increment the left pointer. Else, we we set the right pointer equal to mid since the window of k closest elements will not be to the right of the mid point. Once the pointers meet, we return the values from the left pointer to the kth position which is calculated as left pointer plus k. Time complexity = O(logn + k)

## Question 3
Create an empty list called min_heap which will be used to add the k elements. The first for loop will iterate through the nums list k times and push it to the heap.
The second for loop will iterate through all the remainding elements if k is less than the length of the list nums. Each element is compared to the smallest element, which is the element at index 0, in min_heap. If nums[i] is greater than min_heap[0] then we pop the element at index 0 of the heap and push nums[i]. Once the for loops are done we can print the result. Time complexity = O(Nlogk), n being the total number of elements in the nums list and k being the number of largest elements.

## Question 4


## Question 5
