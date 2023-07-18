import random
import turtle
import time


def create_grid(rows, cols):
    grid = [[0 for i in range(cols)] for j in range(rows)]
    return grid


def generate_maze(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False for i in range(cols)] for j in range(rows)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []

    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    visited[row][col] = True
    stack.append((row, col))

    while len(stack) > 0:
        row, col = stack[-1]
        neighbors = []

        for i in range(4):
            new_row = row + dx[i]
            new_col = col + dy[i]

            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and not visited[new_row][new_col]:
                neighbors.append((new_row, new_col))

        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            stack.append(chosen_neighbor)
            visited[chosen_neighbor[0]][chosen_neighbor[1]] = True
            grid[row][col] |= 1 << i
            grid[chosen_neighbor[0]][chosen_neighbor[1]] |= 1 << ((i + 2) % 4)
        else:
            stack.pop()


def draw_maze(grid):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(10)

    rows = len(grid)
    cols = len(grid[0])

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()

    for row in range(rows):
        for col in range(cols):
            for i in range(4):
                if not (grid[row][col] & (1 << i)):
                    turtle.forward(600 / rows)
                    turtle.left(90)
            turtle.forward(600 / rows)

        turtle.penup()
        turtle.goto(-300, -300 - (row + 1) * 600 / rows)
        turtle.setheading(0)
        turtle.pendown()


def main():
    grid = create_grid(10, 10)
    generate_maze(grid)
    draw_maze(grid)

    turtle.mainloop()


if __name__ == '__main__':
    main()


