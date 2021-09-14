from utilities import sud_check, get_remain, get_sub_box, print_sudo
from generate import sudo

import unittest
import json

Test_file_path = 'test_sudo.json'
Test_file_void_path = 'test_sudo_void.json'

print("#####################################")
print("##############  TEST  ###############")
print("#####################################")

class test_general(unittest.TestCase):
    def setUp(self):
        self.test_obj = sudo(3)

    def test_fill_next_number(self):
        self.test_obj = sudo(3)
        self.test_obj.fill_next_number(8)
        print_sudo( self.test_obj.data, 3 )
        self.test_obj = sudo(3)

    def test_generate_sudo(self):
        size = 3
        self.test_obj = sudo(size)
        self.test_obj.generate()
        print_sudo( self.test_obj.data, size )
        self.test_obj = sudo(size)

class test_get_sub_box(unittest.TestCase):
    def setUp(self):
        with open( Test_file_path ) as file:
            self.test_sudo = json.load(file)

    def test_sub(self):
        test_obj_1 = [
            [5,3,4],
            [6,7,2],
            [1,9,8],
        ]
        test_obj_2 = [
            [7,6,1],
            [8,5,3],
            [9,2,4],
        ]
        test_obj_3 = [
            [2,8,4],
            [6,3,5],
            [1,7,9],
        ]
        self.assertEqual( get_sub_box(self.test_sudo,3,(0,0)), test_obj_1 )
        self.assertEqual( get_sub_box(self.test_sudo,3,(1,1)), test_obj_2 )
        self.assertEqual( get_sub_box(self.test_sudo,3,(2,2)), test_obj_3 )

class test_remain(unittest.TestCase):
    def setUp(self):
        with open( Test_file_void_path ) as file:
            self.test_sudo = json.load(file)
        self.test_obj = get_remain(_size=3)
    
    def test_get_remain_r(self):
        test_data = ( [2,3,5,6,7,8],[1,2,4,6,8,9] )
        self.assertEqual( self.test_obj.get_remain_row( self.test_sudo, 0 ), test_data )
    
    def test_get_remain_c(self):
        test_data = ( [2,6,7,8],[1,2,3,9] )
        self.assertEqual( self.test_obj.get_remain_col( self.test_sudo, 0 ), test_data )

    def test_get_remain_box(self):
        test_data = ( [(0,2),(1,1),(1,2),(2,0)],[1,2,4,7] )
        self.assertEqual( self.test_obj.get_remain_box( self.test_sudo, (0,0) ), test_data )

    def test_counter(self):
        test_data = 3
        self.assertEqual( self.test_obj.count_incidences( self.test_sudo, 5 ), test_data )


class test_check(unittest.TestCase):
    def setUp(self):
        with open( Test_file_path ) as file:
            self.test_sudo = json.load(file)
        self.test_obj = sud_check(_size=3)
        # print(self.test_sudo)

    def test_check_row(self):
        self.assertEqual( self.test_obj.check_row(self.test_sudo,1,0),True )
        self.assertEqual( self.test_obj.check_row(self.test_sudo,0,0),False )


    def test_check_col(self):
        self.assertEqual( self.test_obj.check_col(self.test_sudo,1,0),True )
        self.assertEqual( self.test_obj.check_col(self.test_sudo,0,0),False )
        

    def test_check_box(self):
        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(0,0)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(0,0)),False )

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(0,1)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(0,1)),False )    

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(0,2)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(0,2)),False )   

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(1,0)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(1,0)),False )  

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(1,1)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(1,1)),False )   

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(1,2)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(1,2)),False )   

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(2,0)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(2,0)),False ) 

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(2,1)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(2,1)),False )  

        self.assertEqual( self.test_obj.check_box(self.test_sudo,1,(2,2)),True )
        self.assertEqual( self.test_obj.check_box(self.test_sudo,0,(2,2)),False )

if __name__ == '__main__':
    unittest.main(module=None)