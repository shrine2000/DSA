"""
# question - https://leetcode.com/discuss/interview-question/3515163/Google-interview-question

Given array of intervals. find the maximum intersecting interval pair. 
For eg. given intervals [1, 100], [1000, 2000], [50, 200], [60, 80] the maximum intersecting interval pair is [60,80]. 

Solution :

create two lists, one only stores starting points and another stores ending points. sort them

for each segment, find how many segments end before it starts and how many start after it ends using binary search.

total ct minus non-overlapped ct equals overlapped ct


"""

