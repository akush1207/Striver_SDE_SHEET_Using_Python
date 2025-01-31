from typing import List

def setZero(matrix:List[List[int]])->None:
    row=len(matrix)
    col=len(matrix[0])
    col0=1
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0

    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if matrix[0][0]==0:
        for i in range(col):
            matrix[0][i]=0

    if col0==0:
        for i in range(row):
            matrix[i][0]=0
            
def main():
    rows=int(input('Enter the no. of rows:'))
    matrix=[]
    for i in range(rows):
        row=list(map(int,input(f'Enter row {i+1} elements:').split()))
        matrix.append(row)
    print('Matrix:',matrix)
    setZero(matrix)
    print('Matrix:',matrix)
    
main()