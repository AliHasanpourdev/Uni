def can_water_exit(matrix, start_x, start_y):
    m, n = len(matrix), len(matrix[0])
    stack = [(start_x, start_y)]
    stack_set = set(stack)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n
    
    def dfs(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in stack_set and matrix[nx][ny] < matrix[x][y]:
                stack.append((nx, ny))
                stack_set.add((nx, ny))
                dfs(nx, ny)
    
    dfs(start_x, start_y)
    
    def result(stack, rows, cols, matrix):
        if len(stack) == 1:
            return False

        for row, col in stack:
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                flag = True
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] <= matrix[row][col]:
                        flag = False
                        break
                if flag:
                    return True
        return False
    
    if result(stack, m, n, matrix):
        for i in sorted(stack):
            print(i)
    else:
        print('False')


def main() :
    number_of_row, number_of_col = list(map(int, input().split()))
    start_row, start_col = list(map(int, input().split()))
    map_matrix = []
    for i in range(number_of_row):
        map_matrix.append(list(map(int, input().split())))

    can_water_exit(map_matrix, start_row, start_col)

if __name__=="__main__" :
    main()