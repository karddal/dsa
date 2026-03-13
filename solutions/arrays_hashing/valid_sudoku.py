# 36 Valid Sudoku

# Approach - we need to be able to check which numbers we have seen in each
# row in O(1) time, so this signals we should use a hashmap of sets.
# We can use an early return to immediately stop if we find something making the
# sudoku invalid.

# Time: O(1) as fixed size board
# Space: O(1) as fixed size board

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[row])):
                current = board[row][column]

                if current == ".":
                    continue

                # For boxes, convert 0-8 of row, column into 0-2 of box.
                # 0..=2 = 0, 3..=5 = 1, 6..=8 = 2

                if (
                    current in rows[row]
                    or current in columns[column]
                    or current in boxes[(row // 3, column // 3)]
                ):
                    return False

                rows[row].add(current)
                columns[column].add(current)
                boxes[(row // 3, column // 3)].add(current)

        return True
