#!/usr/bin/env python
# coding=utf-8

matrix_2d =  [[0 for col in range(10)] for row in range(8)]

def init():
    matrix_2d[0][5]=3
    matrix_2d[0][0]=2


def printmatrix(msg):
    print(msg)
    for i in range(8):
        s=""
        for j in range(10):
            s= s+ str( matrix_2d[i][j]) + "   "
        print(s)

def modifymatrix(x,y):
    if (matrix_2d[x][y]==0):
        matrix_2d[x][y]=1

if __name__ == '__main__':
    init()
    printmatrix(" first year")
