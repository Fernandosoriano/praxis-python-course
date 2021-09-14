from utilities import sud_check, get_remain, get_sub_box, print_sudo
from generate import sudo

import random
from datetime import datetime
random.seed(datetime.now())

import csv


if __name__ == '__main__':
    sudoku_size = 3
    generator = sudo(sudoku_size)
    generator.generate()
    with open("last_sudoku.csv",'w') as file:
        csv_writer= csv.writer(file, delimiter=',', quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        for item in generator.data:
            csv_writer.writerow(item)