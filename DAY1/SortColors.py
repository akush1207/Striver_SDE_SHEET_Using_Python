from typing import List
def sortColor(nums:List[float])->None:
    low=0
    mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
def main():
    nums=list(map(int,input('Enter array elements:').split()))
    print('nums',nums)
    sortColor(nums)
    print('nums:',nums)
main()