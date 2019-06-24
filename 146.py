# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4


class LinkNode(object):
    def __init__(self,key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

    def __str__(self):
        s = ""
        cur = self
        while cur:
            s = s + str(cur.val)
            if cur.next:
                s = s + " -> "
            cur = cur.next
        return s


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkNode(0, 0)
        self.tail = LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.bucket = {}

    def _remove_from_list(self, node: LinkNode):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        node.next = None
        node.pre = None

    def _insert_to_head(self, node: LinkNode):
        next = self.head.next
        node.next = next
        next.pre = node
        self.head.next = node
        node.pre = self.head

    def get(self, key: int) -> int:
        v = self.bucket.get(key)
        if v:
            self._remove_from_list(v)
            self._insert_to_head(v)
            return v.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        v = self.get(key)
        # 如果存在，则更新
        if v > 0:
            self.bucket.get(key).val = value
            return None
        # 不存在，新增
        node = LinkNode(key, value)
        # 1. 插入到双向链表头部
        self._insert_to_head(node)
        # 2. 添加到map中
        self.bucket[key] = node
        # 3. 检测容量，超出则移除队尾元素
        if self.capacity < len(self.bucket):
            will_delete = self.tail.pre
            self._remove_from_list(will_delete)
            self.bucket.pop(will_delete.key)
        return None

# from collections import OrderedDict
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = OrderedDict()  # OrderedDict 记住了字典元素的添加顺序
#         self.remain = capacity  # 容量 大小
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         v = self.dic.pop(key)
#         self.dic[key] = v  # 被获取 刷新最近使用
#         return v
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.pop(key)  # 如果字典中有先弹出 再加入
#         else:  # 没有
#             if self.remain > 0:  # 字典未满
#                 self.remain -= 1  # 剩余容量 -1
#             else:  # 字典已满 弹出最近最少使用的，最老的元素
#                 self.dic.popitem(last=False)
#         self.dic[key] = value


if __name__ == '__main__':
    cache = LRUCache(2)
    assert cache.get(2) == -1
    assert not cache.put(2, 6)
    assert cache.get(1) == -1
    assert not cache.put(1, 5)
    assert not cache.put(1, 2)
    assert cache.get(1) == 2
    assert cache.get(2) == 6

    cache = LRUCache(2)
    assert not cache.put(1, 1)
    assert not cache.put(2, 2)
    assert cache.get(1) == 1
    assert not cache.put(3, 3)
    assert cache.get(2) == -1
    assert not cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)