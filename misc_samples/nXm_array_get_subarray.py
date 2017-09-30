"""
Print all rectangles in 2*2 array
"""
r, c = 2,4
arr = "1 2 3 4 5 6 7 8".split()
msum = arr[0]

for row in range(r):
    for col in range(c):
        for row1 in range(row,r):
                
            for col1 in range(col,c):
                
                for row2 in range(row,row1+1):
                    
                    for col2 in range(col,col1+1):
                        
                        print(arr[row2*c+col2], end='')
                    
                print('')