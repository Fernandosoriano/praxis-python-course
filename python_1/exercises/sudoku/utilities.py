def get_sub_box(sud:list,size:int,box_indexs:tuple)->list:
    init_row = box_indexs[0]*size
    init_col = box_indexs[1]*size
    return [ [ sud[row][col] for col in range(init_col,init_col+size) ] for row in range( init_row, init_row+size ) ]

def print_sudo(sud:list,size):
    temp_str = ''
    temp_btw = ''
    print()
    for row in range( size**2 ):
        for col in range( size**2 ):
            if( sud[row][col]==0 ):
                temp_str+='_ '
            else:
                temp_str+=str(sud[row][col])+' '
            if(col!= 0 and (col+1)%size==0):
                temp_str+="| "
        print(temp_str)
        if(row!=0 and (row+1)%size==0):
            for item in range( len(temp_str) ):
                temp_btw+='='
            print(temp_btw)
        temp_str=''
        temp_btw=''


class get_remain:
    def __init__(self,_size):
        self.size = _size

    def count_incidences(self,sud:list,num:int):
        counter = 0
        for row in range( len(sud) ):
            for col in range( len(sud[0]) ):
                if(sud[row][col]==num):
                    counter+=1
        return counter

    def get_remain_row(self,sud:list,row_index:int):
        remain_positions = []
        total_numbers = { item for item in range(1,self.size**2+1) }
        present_numbers = []
        for col in range(self.size**2):
            if(sud[row_index][col]==0):
                remain_positions.append( col )
            else:
                present_numbers.append( sud[row_index][col] )
        temp_remain = list( total_numbers - set( present_numbers ) )
        temp_remain.sort()
        return remain_positions, temp_remain
        
    def get_remain_col(self,sud:list,col_index:int):
        remain_positions = []
        total_numbers = { item for item in range(1,self.size**2+1) }
        present_numbers = []
        for row in range(self.size**2):
            if(sud[row][col_index]==0):
                remain_positions.append( row )
            else:
                present_numbers.append( sud[row][col_index] )
        temp_remain = list( total_numbers - set( present_numbers ) )
        temp_remain.sort()
        return remain_positions,  temp_remain
    
    def get_remain_box(self,sud:list,box_indexs:tuple):
        remain_positions = []
        total_numbers = { item for item in range(1,self.size**2+1) }
        present_numbers = []
        sub_box = get_sub_box( sud, self.size, box_indexs )
        for row in range(self.size):
            for col in range(self.size):
                if(sub_box[row][col]==0):
                    remain_positions.append( (row,col) )
                else:
                    present_numbers.append( sud[row][col] )
        temp_remain = list( total_numbers - set( present_numbers ) )
        temp_remain.sort()
        return remain_positions,  temp_remain

    def get_remain_box_all(self,sud:list):
        remain_positions = []
        for row in range(self.size**2):
            for col in range(self.size**2):
                if(sud[row][col]==0):
                    remain_positions.append( (row,col) )
        return remain_positions



class sud_check:
    def __init__(self,_size):
        self.size=_size

    def check_row(self,sud:list,num:int,row_index:int)->bool:
        return (num in sud[row_index])

    def check_col(self,sud:list,num:int,col_index:int)->bool:
        sud_cols=[ [ sud[row][col] for row in range(len(sud)) ] for col in range(len(sud[0])) ]
        return (num in sud_cols[col_index])

    def check_box(self,sud:list,num:int,box_indexs:tuple)->bool:
        flag = False
        sub_sud = get_sub_box(sud,self.size,box_indexs)
        for row in range(self.size):
            for col in range(self.size):
                # row_index = box_indexs[0]*self.size + row
                # col_index = box_indexs[1]*self.size + col
                # print(sub_sud[row][col])
                if num == sub_sud[row][col]:
                    flag=True
                    break
        return flag