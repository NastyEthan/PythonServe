def construct(matrix):
    length = len(matrix)
    for i in range(length):
        row = len(matrix[i])
        for order in range(row):
            print(matrix[i][order], end='')
        print()

matrix = [[1,2,3],[4,5,6],[7,8,9],[" ",0," "]]

def mat():
  construct(matrix)