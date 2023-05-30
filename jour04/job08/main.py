from os.path import exists


def open_maze():
    maze = []

    file_exists = exists('maze.mz')

    if file_exists:
        with open('maze.mz') as f:
            data = f.read()
            lines = data.split()

            for line in lines:
                maze.append(line)

            return maze
    else:
        print('This file does not exist..')


def moving(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 0), (rows-1, cols-1)

    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    to_visit = [start]

    while to_visit:
        curr_row, curr_col = to_visit.pop(0)
        if (curr_row, curr_col) == end:
            break

        for drow, dcol in neighbors:
            row, col = curr_row + drow, curr_col + dcol
            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == '.' and dist[row][col] == float('inf'):
                to_visit.append((row, col))
                dist[row][col] = dist[curr_row][curr_col] + 1
                parent[row][col] = (curr_row, curr_col)

    row, col = end
    while (row, col) != start:
        maze[row] = maze[row][:col] + 'X' + maze[row][col+1:]
        row, col = parent[row][col]

    f = open('maze-out.mz', 'w+')
    for m in maze:
        f.write(m + '\n')

    f.close()


if __name__ == "__main__":
    labyrinth = open_maze()

    moving(labyrinth)
