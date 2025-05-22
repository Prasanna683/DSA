class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0 :
                nums[j] = nums[i]
                j += 1
        for j in range(j, n):
            nums[j] = 0
        return nums

if __name__ == "__main__"
input_string = input("Enter numbers seperated by spaces")
arr = list(map(int, input_string().strip().split()))
ans = Solution()
print(ans.moveZeroes(arr))
        
