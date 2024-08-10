import numpy as np

rng = np.random.default_rng(seed=22)
A = rng.integers(low=0, high=100, size=100)

min_difference = 2000
right_total = sum(A[1:])
print("Initial right side total:", right_total)
left_total = A[0]
if len(A) == 2:
    min_difference = A[0]-A[1]
    min_difference = abs(min_difference)
    return(min_difference)
else: 
    for num in range(1,len(A)):
        print("Current num", num)
        left_total = A[num] +  left_total
        right_total = right_total - A[num]
        print("right side total", right_total)
        print("left side total", left_total)
        current_difference = left_total - right_total
        current_difference = abs(current_difference)
        print("Current Difference", current_difference)
        if current_difference < min_difference:
            min_difference = current_difference
            
print("Minimum difference returned", min_difference)
