"""
@author Lucas
@date 2019/3/29 21:46
"""


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int((left + right)/2)
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(search([-1, 0, 3, 5, 9, 12], 12))
