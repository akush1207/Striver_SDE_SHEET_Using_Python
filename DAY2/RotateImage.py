from typing import List

def transpose(matrix:List[List[int]])->None:
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
def rotate(matrix:List[List[int]])->None:
    transpose(matrix)
    print('trans:',matrix)
    for i in range(len(matrix)):
        matrix[i].reverse()
    
def main():
    rows=int(input('Enter the no. of rows:'))
    matrix=[]
    for i in range(rows):
        row=list(map(int,input(f'Enter row {i+1} elements:').split()))
        matrix.append(row)
    print('Matrix:',matrix)
    rotate(matrix)
    print('Rotated Matrix:',matrix)

main()