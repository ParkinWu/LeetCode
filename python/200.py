# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
# 并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class UnionFind:
    def __init__(self, grid: List[List[str]]):
        rows = len(grid)
        cols = len(grid[0])

        self.ranks = [0] * (rows * cols)
        self.parents = [0] * (rows * cols)
        self.count = 0

        for r in range(rows):
            for c in range(cols):
                self.parents[r * cols + c] = r * cols + c
                if grid[r][c] == "1":
                    self.count += 1

    def find(self, x: int):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        if self.ranks[x_root] > self.ranks[y_root]:
            self.parents[y_root] = x_root
        elif self.ranks[x_root] < self.ranks[y_root]:
            self.parents[x_root] = y_root
        else:
            self.parents[x_root] = y_root
            self.ranks[y_root] += 1
        self.count -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        uf = UnionFind(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        uf.union(r * cols + c, (r - 1) * cols + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        uf.union(r * cols + c, r * cols + c - 1)
        return uf.count


if __name__ == '__main__':
    s = Solution()
    assert s.numIslands([["1", "1", "1", "1", "0"],
                         ["1", "1", "0", "1", "0"],
                         ["1", "1", "0", "0", "0"],
                         ["0", "0", "0", "0", "0"]]) == 1

    assert s.numIslands([["1", "1", "0", "0", "0"],
                         ["1", "1", "0", "0", "0"],
                         ["0", "0", "1", "0", "0"],
                         ["0", "0", "0", "1", "1"]]) == 3


