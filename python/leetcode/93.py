# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/restore-ip-addresses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def is_valid(self, addr: str) -> bool:
        n = len(addr)
        if n == 0 or n > 3:
            return False
        if n > 1 and addr[0] == '0':
            return False
        return 0 <= int(addr) <= 255

    def backtracking(self, s: str, start: int, list: List[str], ans: List[List[str]]):
        if len(list) == 4 and start == len(s):
            ans.append(list.copy())
            return

        for i in range(1, 4):
            address = s[start:start + i]
            if not self.is_valid(address):
                continue
            self.backtracking(s, start + i, list + [address], ans)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        ans = []
        self.backtracking(s, 0, [], ans)
        return list(map(lambda l: '.'.join(l), ans))


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))