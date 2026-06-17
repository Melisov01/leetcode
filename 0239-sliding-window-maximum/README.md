We create a deque, keep the biggest element as the first element and have items sorted in descending order. In the deque we store only the indices of elements. The moment the index of the first element is less than the left pointer we pop it, because it means that the first element is out of the window. Before moving the left pointer we store the max value

We pop elements from the right if the new element is bigger than the last element in the deque.

