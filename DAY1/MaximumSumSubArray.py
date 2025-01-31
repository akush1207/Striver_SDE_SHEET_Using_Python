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
    num=(int(input('Enter the no. of elements:')))
    nums=[]
    print('Enter array elements:')
    for i in range(num):
        nums.append(int(input()))
    print('Max Profit:',maxsumSubarray(nums))
main()