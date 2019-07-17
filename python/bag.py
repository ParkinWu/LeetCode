# print("adfafd")
# 最大背包

map = {"A": (1, 400), "B": (2, 1000), "C": (3, 500), "D": (5, 2000) }
bagSize = 10

# 假设有了一个函数，MaxCost(背包剩余容量, 可选商品)，返回能装下的最大价值的物品


def MaxCost(leftCap, S):
    if len(map) == 0:
        return 0
    (name, (size, cost)) = S.popitem()
    if size > leftCap:
        return 0
    maxCostWithA = cost + MaxCost(leftCap - size, S)
    maxCostWithOutA = MaxCost(leftCap, S)
    if maxCostWithA > maxCostWithOutA:
        print("choose", name)
    return max(maxCostWithA, maxCostWithOutA)

print(MaxCost(bagSize, map))