# pascal triangle  input -> number of rows (n=4)
'''
1
121
1331
14641
'''

numRows = int(input("ENTER THE NUMBER OF ROWS FOR PASCAL TRIANGLE: "))

def pascal(numRows):
    triangle =[]

    for i in range(numRows):
        row = [None] *(i+1)
        row[0], row[-1] = 1,1
        
        for j in range(1,i):
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]

        triangle.append(row)
    return triangle

print(pascal(numRows))