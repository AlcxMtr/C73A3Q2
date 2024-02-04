nums = [3, -4, 2, -1, 3, 4, -8, 7, -1]

def maxSubArray(nums):
    output = recMax(nums, 0, len(nums))
    print("Max subArray sum: " + str(output[3]))
    print("Found at: [" + str(output[6]) + ", " + str(output[7]) + "]")

# Input arguments: 'nums' is the list of numbers, 'first' is the first index, 'last' is the last index,
def recMax(nums, first, last):
    length = last-first
    if length == 1:
        # [full_sum, left_max, right_max, max_sum, left_end, right_start, left_index, right_index]
        return [nums[first], nums[first], nums[first], nums[first], first, first, first, first]
    half = length//2
    left = recMax(nums, first, first+half)
    right = recMax(nums, first+half, last)
    full_sum = left[0] + right[0]
    part_sum = left[2] + right[1]

    # left_max = max(left[1], right[1] + left[0])
    join_right = right[1] + left[0]
    if left[1] > join_right: 
        left_max = left[1]
        left_end = left[4]
    else:
        left_max = join_right
        left_end = right[4]

    # right_max = max(right[2], left[2] + right[0])
    join_left = left[2] + right[0]
    if right[2] > join_left: 
        right_max = right[2]
        right_start = right[5]
    else:
        right_max = join_left
        right_start = left[5]

    # max_sum = max(part_sum, left[3], right[3])
    if left[3] > right[3]:
        max_sum = left[3]
        left_index = left[6]
        right_index = left[7]
    else:
        max_sum = right[3]
        left_index = right[6]
        right_index = right[7]
    if part_sum > max_sum:
        max_sum = part_sum
        left_index = left[5]
        right_index = right[4]
        
    return [full_sum, left_max, right_max, max_sum, left_end, right_start, left_index, right_index]
    # Returns a list of 8 elements:
        # [full_sum, left_max, right_max, max_sum, left_end, right_start, left_index, right_index]
        # full_sum is the sum of the subtree
        # left_max is the sum of the maximum subarray starting from the leftmost index
        # right_max is the sum of the maximum subarray starting from the rightmost index
        # max_sum is the sum of the maximum subarray
        # left_end is the rightmost index of the maximum subarray starting from the leftmost index
        # right_start is the leftmost index of the maximum subarray starting from the rightmost index
        # left_index is the leftmost index of the maximum subarray
        # right_index is the rightmost index of the maximum subarray

maxSubArray(nums)
