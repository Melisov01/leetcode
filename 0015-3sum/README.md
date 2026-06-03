First I tried to brute force the solution. Didn't help me, then I thought about the ways to break down the problem, or to be precise how to eliminate options. So I did the sorting, that way we could fix one number and do two sum problem with a fixed number, so we have:

`fixed_number + left_pointer + right_pointer`

when the total number is less than 0 we move the left pointer to increase the sum, when the total number is more than 0 we move the left pointer to the left to decrease the sum. Otherwise we found the combination that sums up to 0 and we add it to our array. 

