# cs497homework4

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
# 