# Author: Chungha Sung

from z3 import *
import sys
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("txtPath", help="Path of txt file", type=str)

    args = parser.parse_args()
    txt_path = args.txtPath

    s = Solver()
    rows, cols = (9, 9)
    v_arr = [[0 for i in range(cols)] for j in range(rows)] 
    for i in range(rows):
        for j in range(cols):
            v_arr[i][j] = Int("v"+str(i)+str(j))
            s.add(0 < v_arr[i][j], v_arr[i][j] < 10)

    # the elements of each row should be different 
    for i in range(rows):
        for j in range(cols):
            for k in range(j+1, cols):
                s.add(v_arr[i][j] != v_arr[i][k])

    # the elements of each column should be different
    for i in range(cols):
        for j in range(rows):
            for k in range(j+1, rows):
                s.add(v_arr[j][i] != v_arr[k][i])

    # the elements for each subgrid should be different
    t_arr = [[0 for i in range(cols)] for j in range(rows)] 
    for i in range(rows):
        for j in range(cols):
            t_row = int(i/3)*3 + int(j/3)
            t_col = i*3 + j - t_row*3
            t_arr[t_row][t_col] = v_arr[i][j]

    # the elements of each row of t_arr should be different 
    for i in range(rows):
        for j in range(cols):
            for k in range(j+1, cols):
                s.add(t_arr[i][j] != t_arr[i][k])

    a_arr = [[0 for i in range(cols)] for j in range(rows)] 

    # read input file
    file1 = open(txt_path, 'r') 
    Lines = file1.readlines() 

    r_cnt = 0
    for line in Lines:
        each_line = line.strip()
        c_cnt = 0
        for i in range(0,len(each_line)):
            a_arr[r_cnt][c_cnt] = line[i]
            if line[i] != 'x':
                s.add(v_arr[r_cnt][c_cnt] == int(line[i]))
            c_cnt = c_cnt + 1
        r_cnt = r_cnt + 1

    # print input
    print("Given sudoku question is ..")
    for i in range(rows):
        print(*a_arr[i])

    print("----------------------")
    if s.check() == unsat:
        print("There is no satisfiable model for the input.")
    else:
        print("There is a satisfiable model for the input.")
        m = s.model()
        for i in range(rows):
            for j in range(cols):
                if a_arr[i][j] == 'x':
                    a_arr[i][j] = m[v_arr[i][j]]

        # print the answer
        print("========= Answer ========")
        for i in range(rows):
            print(*a_arr[i])


if __name__ == "__main__":
    main()

