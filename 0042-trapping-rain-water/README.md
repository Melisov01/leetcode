Two pointers idea, nothing fancy. Start from two ends of the array, and check which wall is smaller. If the left wall is smaller, work with that case:

we check if current value of left is bigger than our left max, if it is then we have a new left max, otherwise we got a trapped water and can calculate it for the position `water[i] = min(max_left, max_right) - height[i]` and add to total water

The mirrored approach is used for the right side