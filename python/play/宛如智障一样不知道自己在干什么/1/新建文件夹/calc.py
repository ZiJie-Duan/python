#!/usr/bin/env python
# coding=utf-8

matrix_2d = [[0] * 10] * 8

def init():
    

    

def printmatrix(msg):
    print(msg)
    for i in range(8):
        s=""
        for j in range(10):
            s= s+ str( matrix_2d[i][j]) + "   "
        print(s)



if __name__ == '__main__':
    init()
    printmatrix(" first year")

