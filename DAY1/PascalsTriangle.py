from typing import List
def generateBruteForce(numRows:int)->List[List[int]]:
    pascal=[]
    for i in range(numRows):
        row=[]
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                row.append(pascal[i-1][j]+pascal[i-1][j-1])
        pascal.append(row)
    return pascal
def generateOptimized(numRows:int)->List[List[int]]:
    pascal=[]
    for i in range(numRows):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=pascal[i-1][j]+pascal[i-1][j-1] 
        pascal.append(row)
    return pascal           
def main():
    numRows=int(input('Enter the no. of rows:'))
    print('Pascal Triangle:',generateBruteForce(numRows))
    print('Pascal Triangle:',generateOptimized(numRows))
main()
    