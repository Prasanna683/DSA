class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        ind = n - k

        nums[0 : ind] = nums[0 : ind][::-1]
      
        nums[ind : n] = nums[ind : n][::-1]
     
        nums[0 : n] = nums[::-1]
        return nums
        
if __name__ == "__main__"
input_string = input("Enter numbers seperated by spaces")
k = int(input("Enter a number"))
arr = list(map(int, input_string().strip().split()))
ans = Solution()
print(ans.rotate(arr, k))


      
