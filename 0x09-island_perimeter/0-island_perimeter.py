#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell contains land (has a value of 1)
            if grid[i][j] == 1:
                # Add 4 to the perimeter for each land cell
                perimeter += 4

                # Check if the cell above the current cell is also land
                if i > 0 and grid[i - 1][j] == 1:
                    """Subtract 2 from the perimeter for
                    shared edge with the cell above"""
                    perimeter -= 2

                """Check if the cell to the left of the
                current cell is also land"""
                if j > 0 and grid[i][j - 1] == 1:
                    """Subtract 2 from the perimeter for
                    shared edge with the cell to the left"""
                    perimeter -= 2
    return perimeter
