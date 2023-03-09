import random
class jabba():
    def __init__(self):
        data,snakes,matrix = self.extract_data(self.load_file())
        self.matrix = matrix
        self.snakes = snakes
        self.collumns = data[0]
        self.row = data[1]

    def extract_data(self,data):
        lines = data
        data = []
        for line in lines:
            row = []
            chars = line.split(' ')
            for char in chars:
                if char != ' ':
                    row.append(char.strip('\n'))
            data.append(row)
        line_1 = data[0]
        line_2 = data[1]
        data.pop(0)
        data.pop(0)
        matrix = []
        for row in data:
            new_row = []
            for item in row:
                if item == '*':
                    item = 5
                else:
                    item = int(item)
                new_row.append((item,-1))
            matrix.append(new_row)
        return((line_1,line_2,matrix))
    
    def load_file(self):
        with open('input.txt','r') as f:
            lines = f.readlines()
        return(lines)

    def get_surrounding(self,c,r):
        matrix = self.matrix
        up = matrix[r-1][c]
        x,y = up
        up = (x,y,"up")
        if r+1 == len(matrix):
            down = matrix[0][c]
        else:
            down = matrix[r+1][c]
        x,y = down
        down = (x,y,"down")
        left = matrix[r][c-1]
        x,y = left
        left = (x,y,"left")
        if c+1 == len(matrix[r]):
            right = matrix[r][0]
        else:
            right = matrix[r][c+1]
        x,y = right
        right = (x,y,"right")
        return([up,down,left,right])

    def deploy_snake(self,num_snake,rows,colums):
        start_pos=[]
        duplicate=True
        for x in range (0 , num_snake):
                row_cord=random.randint(0,rows-1)
                column_cord=random.randint(0,colums-1)
                start_pos.append([row_cord,column_cord])

        while (duplicate ==True):
                duplicate=False
                for i in range(len(start_pos)):
                    for j in range(i+1, len(start_pos)):
                        if start_pos[i] == start_pos[j]:
                            duplicate==True
                            row_cord=random.randint(0,rows-1)
                            column_cord=random.randint(0,colums-1)
                            start_pos[i][j].append([row_cord,column_cord])

        return start_pos 
