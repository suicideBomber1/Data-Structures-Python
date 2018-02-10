def search_from(maze, start_row, start_col):
    maze.update_position(start_row, start_col)
    # Base Cases
    # 1. Check if we run into an obstacle
    if maze[start_row][start_col] == OBSTACLE:
        return False
    # 2. We have a square that has already been explored
    if maze[start_row][start_col] == TRIED:
        return False
    # 3. Success ! Outside edge not occupied by obstacle
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_col, TRIED)
    # 4. Otherwise there is no solution

    # Recursively use the one step until there is a conclusion

    found = search_from(maze, start_row - 1, start_col) or \
        search_from(maze, start_row + 1, start_col) or \
        search_from(maze, start_row, start_col - 1) or \
        search_from(maze, start_row, start_col + 1)

    if found:
        maze.update_position(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_position(start_col, start_col, DEAD_END)
    return found
