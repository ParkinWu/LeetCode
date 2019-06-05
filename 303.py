from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        targets = []
        n = len(nums)
        last = 0
        for i in range(0, n):
            sum = nums[i] + last
            last = sum
            targets.append(sum)
        self.targets = targets

    def sumRange(self, i: int, j: int) -> int:
        return self.targets[j] - self.targets[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.targets)
    sum02 = obj.sumRange(0, 2)

    print(sum02)