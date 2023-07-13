"""
https://youtu.be/4tYoVx0QoN0g
"""

import random
import turtle
import time

def get_a_random_bits_list(leng):

    seq = []
    for i in range(leng):
        seq.append(random.choice([0, 1]))
    return seq


def create_random_matrix_1(leng):

    list = [get_a_random_bits_list(leng) for i in range(leng)]
    return list


def edge_turner_hor(matrix):

    for i in range(len(matrix)):
        if matrix[0][i] == 1:
            matrix[0][i] = 2
    for i in range(len(matrix)):
        if matrix[len(matrix)-1][i] == 1:
            matrix[len(matrix)-1][i] = 2


def edge_turner_vert(matrix):
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            matrix[i][0] = 2
    for i in range(len(matrix)):
        if matrix[i][len(matrix)-1] == 1:
            matrix[i][len(matrix)-1] = 2


def line_turner(matrix, line):
    for i in range(len(matrix)):
        if matrix[line][i] == 0:
            pass
        elif (matrix[line][i] == 1 or matrix[line][i] == 3) and ((matrix[line-1][i] == 2) or (matrix[line][i-1] == 2) or (matrix[line][i+1] == 2) or (matrix[line+1][i] == 2)):
            matrix[line][i] = 2
        elif matrix[line][i] != 2:
            matrix[line][i] = 3


def colum_turner(matrix, column):
    for i in range(len(matrix)):
        if matrix[i][column] == 0:
            pass
        elif (matrix[i][column] == 1 or matrix[i][column] == 1) and ((matrix[i-1][column] == 2) or (matrix[i+1][column] == 2) or (matrix[i][column+1] == 2) or (matrix[i][column-1] == 2)):
            matrix[i][column] = 2
        elif matrix[i][column] != 2:
            matrix[i][column] = 3


def matrix_visualiser_start(matrix):

    le = len(matrix)+1
    turtle.penup()
    turtle.pensize(2)
    turtle.speed(1000)
    for x in range(le):
        turtle.goto(-500, 500-100*x)
        turtle.pendown()
        turtle.goto(-500+(le-1)*100, 500-100*x)
        turtle.penup()
    for x in range(le):
        turtle.goto(-500+x*100, 500)
        turtle.pendown()
        turtle.goto(-500+x*100, 500-(le-1)*100)
        turtle.penup()


def matrix_visualiser_filler(matrix):
    le = len(matrix)
    turtle.pensize(50)
    for i in range(le):
        for c in range(le):
            turtle.goto(-450+i*100, 450-c*100)
            if matrix[c][i] == 0:
                turtle.color("white")
            if matrix[c][i] == 1:
                turtle.color("black")
            if matrix[c][i] == 2:
                turtle.color("blue")
            if matrix[c][i] == 3:
                turtle.color("red")
            turtle.pendown()
            turtle.goto(-450+i*100+1, 450-c*100)
            turtle.penup()
    turtle.pensize(2)
    turtle.color("black")


def island_checker(matrix):
    leng = len(matrix)
    edge_turner_vert(matrix)
    edge_turner_hor(matrix)
    for z in range(leng*1000):
        for v in range(leng):
            colum_turner(matrix, v)
            line_turner(matrix, v)


def matrix_reverter(matrix):

    leng = len(matrix)
    for c in range(leng):
        for i in range(leng):
            if matrix[i][c] == 1 or matrix[i][c] == 2:
                matrix[i][c] = 1
            if matrix[i][c] == 3:
                matrix[i][c] = 0
            if matrix[i][c] == 0:
                pass


def main():

    built_in_matrix = [[0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]
    custom_len = (str(input("custom matrix lenght (leave empty for built in): ")))
    custom_matrix = []
    if custom_len == "":
        custom_matrix = built_in_matrix
    else:
        custom_matrix = create_random_matrix_1(int(custom_len))
    matrix_visualiser_start(custom_matrix)
    print("first matrix \n", custom_matrix)
    matrix_visualiser_filler(custom_matrix)
    time.sleep(1)
    island_checker(custom_matrix)
    print("second matrix \n", custom_matrix)
    matrix_visualiser_filler(custom_matrix)
    matrix_reverter(custom_matrix)
    time.sleep(1)
    print("final matrix \n", custom_matrix)
    matrix_visualiser_filler(custom_matrix)
    time.sleep(1)


main()


