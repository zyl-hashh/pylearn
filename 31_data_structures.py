"""
Python 第 31 课 —— 数据结构：栈、队列、链表

═══════════════════════════════════════════════════════════
为什么要学数据结构？
═══════════════════════════════════════════════════════════

你用了很久 list 和 dict，它们是 Python 帮你实现好的数据结构。
但面试官会问："不用 list 的 append/pop，你能自己实现一个栈吗？"

这节课就是答案——理解三个最基础的数据结构，
知道它们"怎么实现"、"什么时候用"、"Python 里怎么用"。

═══════════════════════════════════════════════════════════
先搞清楚一件事：数据结构 = 数据 + 操作
═══════════════════════════════════════════════════════════

任何数据结构都回答两个问题：
  1. 数据怎么存？（排列方式）
  2. 支持哪些操作？（增删改查）

就像你的实验样品——
  存法：试管架（list）= 一排按顺序放，标签本（dict）= 按名字找
  操作：取第 3 个 vs 找名叫 "WA3" 的
"""

# ═══════════════════════════════════════════════════════════
# 第 1 部分：栈 (Stack)
# ═══════════════════════════════════════════════════════════

print("=" * 60)
print("1. 栈 (Stack) — 后进先出，像一摞盘子")
print("=" * 60)

print("""
生活中：
  你洗了一摞盘子，最后洗的放在最上面（push），
  要用的时候从最上面拿（pop）。最先洗的在最下面，
  最后才轮得到。

计算机里：
  - 浏览器"后退"按钮 → 栈
  - 撤销操作 (Ctrl+Z) → 栈
  - Python 的函数调用 → 调用栈 (call stack)
    （你在 debug 时看到的 Traceback 就是调用栈！）

核心操作（只有两个）：
  push(元素)  → 放到栈顶
  pop()       → 从栈顶取出

特点：只能操作栈顶，不能从中间拿。
""")

# --- 用 list 实现栈 ---
print("用 Python list 实现栈：")

class Stack:
    """用 list 封装的栈——list 的 append/pop 天然就是栈"""

    def __init__(self):
        self.items = []               # 用 list 存数据

    def push(self, item):
        """压栈——把元素放到栈顶"""
        self.items.append(item)       # list.append = 加到末尾 = 栈顶

    def pop(self):
        """弹栈——从栈顶取出元素"""
        if self.is_empty():
            raise IndexError("栈空了，不能再 pop")
        return self.items.pop()       # list.pop() = 从末尾取出

    def peek(self):
        """看栈顶元素但不取出"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# 演示
stack = Stack()
stack.push("实验A")
stack.push("实验B")
stack.push("实验C")

print("压入了: 实验A → 实验B → 实验C")
print(f"栈顶是什么? {stack.peek()}")   # 实验C（最后压入的）
print(f"弹出一个: {stack.pop()}")      # 实验C（后进先出）
print(f"再弹一个: {stack.pop()}")      # 实验B
print(f"还剩多少? {stack.size()}")     # 1

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 第 2 部分：队列 (Queue)
# ═══════════════════════════════════════════════════════════

print("=" * 60)
print("2. 队列 (Queue) — 先进先出，像排队买饭")
print("=" * 60)

print("""
生活中：
  食堂排队——谁先来谁先打饭。插队到中间是不行的。

计算机里：
  - 打印机队列——先提交的文档先打印
  - 消息队列——先收到的消息先处理
  - BFS（广度优先搜索）——下一节课会用到

核心操作：
  enqueue(元素)  → 加入队尾（入队）
  dequeue()      → 从队头取出（出队）

栈 vs 队列：
  栈: 后进先出 LIFO (Last In First Out) — 从同一端进出
  队列: 先进先出 FIFO (First In First Out) — 一端进另一端出
""")

# --- 用 collections.deque 实现队列 ---
# 为什么不用 list？list.pop(0) 是 O(n)——每次取第一个要移动后面所有元素
# deque 专门为两端操作优化，popleft() 是 O(1)

from collections import deque

class Queue:
    """用 deque 封装的队列"""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """入队——加到队尾"""
        self.items.append(item)

    def dequeue(self):
        """出队——从队头取出"""
        if self.is_empty():
            raise IndexError("队列空了")
        return self.items.popleft()    # 关键：从左边出（队头）

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# 演示
queue = Queue()
queue.enqueue("任务1")
queue.enqueue("任务2")
queue.enqueue("任务3")

print("入队了: 任务1 → 任务2 → 任务3")
print(f"出队: {queue.dequeue()}")      # 任务1（最先入队的！）
print(f"出队: {queue.dequeue()}")      # 任务2
print(f"还剩: {queue.size()}")         # 1


# ═══════════════════════════════════════════════════════════
# 第 3 部分：链表 (Linked List)
# ═══════════════════════════════════════════════════════════

print("──────────────")
print("=" * 60)
print("3. 链表 (Linked List) — 一节扣一节的链子")
print("=" * 60)

print("""
Python 的 list 在内存中是连续存储的（一整块地），
插入到中间需要把后面的元素全部往后移（O(n)）。

链表的每个元素叫"节点 (Node)"，包含两部分：
  data: 存的数据
  next: 指向下一个节点的"箭头"

最后一个节点的 next 指向 None（表示到头了）。

好处：插入/删除不需要移动其他元素，改指针就行 (O(1))
代价：不能像 list 那样直接用下标取第 5 个元素 (O(n))
""")


# 链表节点
class Node:
    """链表的节点——像一个火车车厢，连到下一个"""

    def __init__(self, data):
        self.data = data            # 车厢里装的东西
        self.next = None            # 连接到下一个车厢（目前只挂了这一节）


class LinkedList:
    """单向链表——手动管理节点"""

    def __init__(self):
        self.head = None            # 链表头（第一节车厢）
        self._size = 0

    def append(self, data):
        """在末尾添加一个节点——和 list.append 一样的效果"""
        new_node = Node(data)

        if self.head is None:       # 链表是空的
            self.head = new_node    # 新节点就是头
        else:
            # 从头开始，走到最后一个节点（next 为 None 的那个）
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node # 把最后一个节点的 next 指向新节点
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        """打印链表：Node1 → Node2 → Node3 → None"""
        if self.head is None:
            return "空链表"
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return " → ".join(parts) + " → None"

    def get(self, index):
        """按下标取值（和 list[index] 一样，但要遍历）"""
        if index < 0 or index >= self._size:
            raise IndexError("下标越界")
        current = self.head
        for _ in range(index):       # 走 index 步
            current = current.next
        return current.data


# 演示
ll = LinkedList()
ll.append("WA1")
ll.append("WA2")
ll.append("WA3")

print(f"链表: {ll}")
print(f"长度: {len(ll)}")
print(f"第 1 个: {ll.get(0)}")
print(f"第 2 个: {ll.get(1)}")


# ═══════════════════════════════════════════════════════════
# 第 4 部分：三种结构的对比
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("三种数据结构速查表")
print("=" * 60)
print("""
               栈 (Stack)      队列 (Queue)       链表 (Linked List)
  ────────     ─────────       ──────────         ────────────────
  进出规则     后进先出 LIFO    先进先出 FIFO       按需遍历
  类比         一摞盘子         食堂排队           火车车厢
  插入         push (O(1))      enqueue (O(1))     append (O(1))
  删除         pop (O(1))       dequeue (O(1))     remove (O(1)已知位置)
  查找         不支持随机       不支持随机          O(n)
  Python实现   list             deque              ＜自己写＞

  什么时候用：
  栈   → 撤销操作、括号匹配、函数调用栈、深度优先搜索
  队列 → 打印任务、消息队列、广度优先搜索、缓冲区
  链表 → 需要频繁在中间插入/删除、内存不连续的场景
""")


# ═══════════════════════════════════════════════════════════
# 第 5 部分：实战 — 用栈做括号匹配
# ═══════════════════════════════════════════════════════════

print("=" * 60)
print("实战：用栈检查括号是否匹配")
print("=" * 60)


def is_balanced(expr):
    """检查表达式中的括号是否匹配。
    例: "(a+b)" → True, "((a+b)" → False, "[(])" → False
    """
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in expr:
        if char in "([{":              # 左括号 → 压栈
            stack.append(char)
        elif char in ")]}":            # 右括号 → 弹栈匹配
            if not stack:              # 栈空 = 多了右括号
                return False
            top = stack.pop()
            if top != pairs[char]:     # 不配对
                return False
    return len(stack) == 0             # 栈空 = 全部配对完成


print(f"'(a+b)'         → {is_balanced('(a+b)')}")        # True
print(f"'((a+b)'        → {is_balanced('((a+b)')}")        # False
print(f"'([{}])'        → {is_balanced('([{}])')}")        # True
print(f"'[(])'          → {is_balanced('[(])')}")          # False


# ═══════════════════════════════════════════════════════════
# 练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 用栈实现一个"字符串反转"函数 reverse_string(s)
# 思路：把每个字符 push 进栈，然后逐个 pop 出来

print("练习 1: reverse_string()")
# ↓↓↓ 你的代码 ↓↓↓



print("\n")

# ── 练习 2 ──
# 给上面的 LinkedList 类添加 insert(index, data) 方法
# 在第 index 个位置插入新节点

print("练习 2: LinkedList.insert()")
# ↓↓↓ 你的代码 ↓↓↓



print("\n")

# ── 练习 3 ──
# 用队列模拟"约瑟夫环"问题：
# n 个人围成一圈，每次数到第 k 个人就淘汰，问最后剩下谁？
# 提示: 把所有人入队，然后每次把前面 k-1 个人出队再入队，第 k 个出队

print("练习 3: 约瑟夫环")
# ↓↓↓ 你的代码 ↓↓↓



# ═══════════════════════════════════════════════════════════
# 复习练习（11-13 概念：lambda + 模块）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习："
      "把 Stack 类放到单独的 stack.py 文件里，然后 import 使用")
print("=" * 50 + "\n")

# ↓↓↓ 按提示在 python/ 里创建 stack.py，然后在这里 import ↓↓↓



# ═══════════════════════════════════════════════════════════
# 就业前瞻：数据结构是面试的"第一道门"
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】为什么大厂面试必考数据结构")
print("=" * 50)
print("""
不管你是应聘数据分析、后端开发、还是算法工程师，
面试的第一道技术题大概率是数据结构。

经典面试题（你现在能做的）：
  "用栈实现队列"
    → 准备两个栈，push 进栈1，pop 时把栈1 全部倒到栈2

  "反转链表"
    → 遍历时把每个节点的 next 指向它的前一个节点

  "有效的括号"（刚才已经写过了）
    → LeetCode 第 20 题，高频题，你已经会了

面试官不是要你背代码——是要看你会不会分析"时间和空间复杂度"、
知不知道"为什么用这个结构而不是那个"。这就引出了下节课的内容：
算法与时间复杂度。
""")
