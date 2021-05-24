import time
start = time.time()
numbers = [42, 12, 13, 89, 63, 11]

def selSort(nums):
    # sort nums into ascending order

    n = len(nums)

    # For each position in the list (except the very last)

    for bottom in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]

        sm = bottom                     # bottom is smallest initially
        for i in range(bottom+1, n):    # look at each position
            if nums[i] < nums[sm]:      # this one is smaller
                sm = i                  # remember its index

        # swap smallest item to the bottom
        nums[bottom], nums[sm] = nums[sm], nums[bottom]

    return nums

print(selSort(numbers))

end = time.time()
print(end-start)
