# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
#  
#
# 示例 1：
#
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
# 示例 2：
#
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
# 示例 3：
#
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#  
#
# 提示：
#
# 给出的日期一定是在 1971 到 2100 年之间的有效日期。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/day-of-the-week
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    # Solution 1: 蔡勒公式
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month += 12
            year -= 1

        c = year // 100
        y = year % 100
        m = month
        d = day

        i = (y + y // 4 + c // 4 - 2 * c + (26 * m + 26) // 10 + d - 1) % 7
        return week[i]


if __name__ == '__main__':
    s = Solution()
    assert s.dayOfTheWeek(31, 8, 2019) == "Saturday"
    assert s.dayOfTheWeek(18, 7, 1999) == "Sunday"
    assert s.dayOfTheWeek(15, 8, 1993) == "Sunday"
    assert s.dayOfTheWeek(29, 2, 2016) == "Monday"
