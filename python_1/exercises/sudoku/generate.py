from utilities import print_sudo
import math
import random

class sudo:
    def __init__(self,_size):
        self.size = _size
        self.data = [ [ 0 for col in range(_size**2) ] for row in range(_size**2) ]

    def erase_number(self,number:int):
        for row in range(self.size**2):
            for col in range(self.size**2):
                if(self.data[row][col]==number):
                    self.data[row][col]=0

    def fill_next_number(self,number:int):
        counter = 0
        rows = [row for row in range(self.size**2)]
        cols = [col for col in range(self.size**2)]
        indexs=[]
        for row_box in range(self.size):
            for col_box in range(self.size):
                flag = True
                row = random.choice( [ row for row in range(self.size) ] )
                col = random.choice( [ col for col in range(self.size) ] )
                while(flag):
                    counter+=1
                    if( self.data[row_box*self.size+row][col_box*self.size+col]==0 ):
                        if( ((row_box*self.size+row) in rows)and((col_box*self.size+col) in cols) ):
                            rows.pop( rows.index( row_box*self.size+row ) )
                            cols.pop( cols.index( col_box*self.size+col ) )
                            break
                        else:
                            row = random.choice( [ row for row in range(self.size) ] )
                            col = random.choice( [ col for col in range(self.size) ] )

                    else:
                        row = random.choice( [ row for row in range(self.size) ] )
                        col = random.choice( [ col for col in range(self.size) ] )
                    if counter>self.size**4:
                        return -1
                indexs.append(( row_box*self.size+row, col_box*self.size+ col))
        for idx in indexs:
            self.data[idx[0]][idx[1]]=number



    def generate(self):
        num=0
        while(num<self.size**2):
            val = self.fill_next_number(num+1)
            if(val==-1):
                if num>0:
                    num-=1
                    self.erase_number(num+1)
                else:
                    print(" E R R O R ")
                    return
            else:
                num+=1
