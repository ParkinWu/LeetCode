# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100
# 注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List, Tuple


class Solution:
    def canForward(self, matrix: List[List[int]], visited: List[List[int]], position: List[int], direction: List[int]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        new_position = [position[0] + direction[0], position[1] + direction[1]]
        return 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and not visited[new_position[0]][new_position[1]]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows == 0:
            return []
        if rows == 1:
            return matrix[0]
        cols = len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visted = [[0] * cols for _ in range(rows)]
        directionIndex = 0
        position = [0, 0]
        ans = []
        while True:
            row = position[0]
            col = position[1]
            visted[row][col] = 1
            ans.append(matrix[row][col])
            direction = directions[directionIndex]
            if self.canForward(matrix, visted, position, direction):
                position = [position[0] + direction[0], position[1] + direction[1]]
            elif self.canForward(matrix, visted, position, directions[(directionIndex + 1) % 4]):
                directionIndex = (directionIndex + 1) % 4
                direction = directions[directionIndex]
                position = [position[0] + direction[0], position[1] + direction[1]]
            else:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
