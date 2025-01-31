from typing import List
def maxsumSubarray(nums:List[int])->int:
    maxSum=nums[0]
    currSum=0
    for num in nums:
        if(currSum<0):
            currSum=0
        currSum+=num
        maxSum=max(maxSum,currSum)
    return maxSum
def main():
    nums=list(map(int,input('Enter array elements:').split()))
    print(nums)
    print('Max Profit:',maxsumSubarray(nums))
main()