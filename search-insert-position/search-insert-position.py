# 35. Search Insert Position
# Easy

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

def search_insert_position(nums: list, target: int):
    if target in nums:
        return nums.index(target)
    
    for index, num in enumerate(nums):
        if target > num and index == len(nums) - 1:
            return index + 1
        elif target < num and index == 0:
            return 0
        elif target > num and target < nums[index + 1]:
            return index + 1

def main():
    print(search_insert_position(nums = [1,3,5,6], target = 5))
    print(search_insert_position([1,3,5,6], target = 2))
    print(search_insert_position([1,3,5,6], target = 7))

if __name__ == '__main__':
    main()