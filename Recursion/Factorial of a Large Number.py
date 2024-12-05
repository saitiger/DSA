class Solution:
    def multiply(self, nums, size, multiplier):
        carry = 0
        
        for i in range(size):
            result = (multiplier * nums[i]) + carry
            nums[i] = result % 10
            carry = result // 10
        
        while carry:
            nums[size] = carry % 10
            size += 1
            carry //= 10

    def factorial(self, N):
        nums = [0] * 10000
        nums[0] = 1
        size = 1

        for multiplier in range(2, N + 1):
            self.multiply(nums, size, multiplier)
        
        result = []
        for i in range(size - 1, -1, -1):
            result.append(nums[i])
        
        return result
