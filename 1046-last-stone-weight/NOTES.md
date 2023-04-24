This is a PriorityQueue problem because we need to keep track of the heaviest stones and always choose the two heaviest ones to smash them together.
​
A PriorityQueue is a data structure that provides us with a way to keep the elements sorted, and always have the smallest or largest element at the top. In this case, we want to keep the heaviest elements at the top of the priority queue so that we can easily access them and smash them together.
​
We also need to be able to efficiently remove elements from the middle of the priority queue and add new ones, which can be done in O(log n) time using a priority queue.
​
Therefore, a priority queue is a suitable data structure to solve this problem, and we can use it to keep track of the heaviest stones and repeatedly smash them together until there is at most one stone left.
​