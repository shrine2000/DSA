# https://codeforces.com/blog/entry/93071

"""
Question 1 — N boxes are Arrranged in a line. Each box is colored either with white or black. You can select any number of boxes from the starting and put it behind the last box in the same sequence as it was placed initially. you can perform this operation atmost once. For example string s="wbbb" . In one operation you can select "wb" and from the start and put it behind the last box "b".

Note: you cannot select all the n boxes.

You are required to find the minimum number of boxes whose colors must be reversed so that all the boxes in the sequence are of an alternate color, that is any two adjacent boxes are of different colors.


Input :  5
wwwwwbbww
wwwb
bwww
wwww
bbbbb

Output :
3
1
1
2
2
"""
