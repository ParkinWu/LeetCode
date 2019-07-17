# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:

    def dfs(self, board: List[List[str]], visit: List[List[int]], word: str, index: int, row: int, col: int) -> bool:
        if index == len(word):
            return True
        visit[row][col] = 1
        rows = len(board)
        cols = len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for d in directions:
            (x, y) = (row + d[0], col + d[1])
            if x < 0 or y < 0 or x >= rows or y >= cols or visit[x][y]:
                continue
            if board[x][y] == word[index] and self.dfs(board, visit, word, index + 1, x, y):
                return True
        visit[row][col] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        if rows == 0:
            return False
        if len(word) == 0:
            return True
        cols = len(board[0])
        visit = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    if self.dfs(board, visit, word, 1, i, j):
                        return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([['A']], "A"))
    print(s.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED"))
    print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE"))
    print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB"))
    print(s.exist([["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]]
, "aab"))
    print(s.exist([["a","b","b","b","b","b","b","a"],["a","a","a","b","b","b","a","b"],["a","b","b","b","a","b","a","a"],["b","a","a","b","b","b","a","a"],["a","b","b","b","a","b","b","b"],["b","b","a","a","a","a","b","a"],["b","a","a","b","a","a","a","b"],["a","a","a","b","b","a","b","b"],["b","b","a","a","a","b","b","b"],["a","b","b","a","b","b","b","a"]]
,"babbaabaaabaa"))