"""
Python 第 32 课 —— 算法入门：排序、二分查找、时间复杂度

═══════════════════════════════════════════════════════════
什么是算法？
═══════════════════════════════════════════════════════════

算法 = 解决问题的一系列步骤。
你已经在写算法了：
  - 计算 PSI = Q×1000/log10(Ce) → 数学公式就是算法
  - 对列表排序 → sorted() 背后是 Timsort 算法
  - 在字典里找值 → dict[key] 背后是哈希算法

这节课学两个最基础的算法 + 一个程序员的核心思维方式：时间复杂度。
"""

import time
import random

# ═══════════════════════════════════════════════════════════
# 第 1 部分：时间复杂度 O(n) — 代码有多快？
# ═══════════════════════════════════════════════════════════

print("=" * 60)
print("1. 时间复杂度：不是秒，是"n 翻倍时时间翻多少倍"")
print("=" * 60)

print("""
为什么不用秒来衡量？
  因为同一段代码在 i9 和 i3 上跑的时间不一样。
  时间复杂度衡量的是"增长率"——输入量翻倍，计算量翻多少倍。

五个常见级别（从快到慢）：
""")

def demo_complexity():
    """直观对比不同复杂度"""
    n = 5000

    # O(1) — 常数时间（不管 n 多大，一步搞定）
    start = time.perf_counter()
    result = 42             # 访问一个变量
    t1 = time.perf_counter() - start
    print(f"  O(1)  常数      : {t1:.8f} 秒  (不管 n 多大都一样快)")

    # O(log n) — 对数时间（n 翻倍只多一步）
    import math
    start = time.perf_counter()
    result = int(math.log2(n))
    t2 = time.perf_counter() - start
    print(f"  O(log n) 对数    : {t2:.8f} 秒  (n 翻倍只多一步)")

    # O(n) — 线性时间（n 翻倍时间翻倍）
    start = time.perf_counter()
    total = sum(range(n))
    t3 = time.perf_counter() - start
    print(f"  O(n)  线性       : {t3:.8f} 秒  (n 翻倍时间翻倍)")

    # O(n²) — 平方时间（n 翻倍时间翻 4 倍）
    start = time.perf_counter()
    for i in range(n):
        for j in range(n):
            pass          # 啥都不干，只是跑两层循环
    t4 = time.perf_counter() - start
    # O(n²) 太慢所以缩小 n
    print(f"  O(n²) 平方       : {t4:.6f} 秒  (n={n}, 10倍n=100倍时间!!)")

demo_complexity()

print("""
怎么理解？
  你处理 100 个样品：
    O(1)   → 不管 100 还是 10000 个，一样快
    O(n)   → 100 个要 1 秒，1000 个要 10 秒
    O(log n) → 100 个要 7 步，1000 个要 10 步（只多了 3 步！）
    O(n²)  → 100 个要 1 秒，1000 个要 100 秒（炸了！）

  Python dict 查值 = O(1)，list 查值 = O(n)
  这就是为什么之前说"dict 比 list 快"——不是感觉上的快，
  是数学上的快：dict 不管多大，一次就找到；list 越大越慢。

你的 list 越长，dict 的优势越明显，因为两者的增长率不一样。
""")


# ═══════════════════════════════════════════════════════════
# 第 2 部分：二分查找 — O(log n) 的经典算法
# ═══════════════════════════════════════════════════════════

print("──────────────")
print("=" * 60)
print("2. 二分查找 (Binary Search) — 翻字典找单词的方式")
print("=" * 60)

print("""
你在字典里查 "phosphorus"：
  1. 翻到中间 → 看到 "manganese" → "phosphorus" 在后面
  2. 翻到后一半的中间 → 看到 "silicon" → 在前面
  3. 翻到前一半的中间 → 找到了 "phosphorus"

每次砍掉一半，300 页的字典最多翻 9 次（log₂300 ≈ 8.2）。
如果是顺序查找（从第一页一页页翻），平均 150 次。

这就是"二分查找"——数组必须已排序，然后反复折半。
""")


def binary_search(arr, target):
    """二分查找：在已排序的列表里找 target。
    返回下标，找不到返回 -1。

    arr: 已排序的列表（从小到大）
    target: 要找的值

    过程可视化（找 7）：
      [1,3,5,7,9,11,13]  ← 初始
       L=0     M=3    R=6    M=7 → 找到了！
    """
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2      # 中间位置

        if arr[mid] == target:
            print(f"    找了 {steps} 步，arr[{mid}] = {target}")
            return mid
        elif arr[mid] < target:        # 目标在右边
            left = mid + 1
        else:                          # 目标在左边
            right = mid - 1

    print(f"    找了 {steps} 步，没找到")
    return -1


# 创建排序列表来演示
sorted_data = list(range(1, 101, 3))   # 1, 4, 7, 10, ... 共 34 个元素
print("\n演示二分查找：")
binary_search(sorted_data, 1)          # 找最小的
binary_search(sorted_data, 55)         # 找中间的
binary_search(sorted_data, 100)        # 找最大的
binary_search(sorted_data, 50)         # 不存在的

# 对比：线性查找 vs 二分查找
print("\n性能对比（100 万元素的列表）：")
big_list = list(range(1_000_000))

start = time.perf_counter()
for _ in range(1000):
    # 线性查找：自己写循环找
    found = False
    for x in big_list:
        if x == 999999:
            found = True
            break
print(f"  线性查找 1000 次: {time.perf_counter() - start:.4f} 秒")

start = time.perf_counter()
for _ in range(1000):
    binary_search(big_list, 999999)
print(f"  二分查找 1000 次: {time.perf_counter() - start:.4f} 秒")


# ═══════════════════════════════════════════════════════════
# 第 3 部分：自己实现排序 — 冒泡排序 vs 插入排序
# ═══════════════════════════════════════════════════════════

print("──────────────")
print("=" * 60)
print("3. 排序算法 — 理解 sorted() 背后的原理")
print("=" * 60)


def bubble_sort(arr):
    """冒泡排序 O(n²)：相邻两两比较，大的往后"冒"。

    过程可视化（排 [5,3,8,1]）：
      第 1 轮: [3,5,1,8]  ← 8 冒到最后
      第 2 轮: [3,1,5,8]  ← 5 冒到倒数第二
      第 3 轮: [1,3,5,8]  ← 完成
    """
    n = len(arr)
    arr = arr.copy()          # 不改变原列表
    swaps = 0
    for i in range(n - 1):    # 共 n-1 轮
        swapped = False
        for j in range(n - 1 - i):  # 每轮比较到已排好的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换
                swaps += 1
                swapped = True
        if not swapped:       # 这轮没交换 → 已经排好了
            break
    print(f"  冒泡排序: 交换了 {swaps} 次")
    return arr


def insertion_sort(arr):
    """插入排序 O(n²)：像打牌时整理手牌——摸一张插到合适位置。

    过程可视化（排 [5,3,8,1]）：
      摸 3: [3,5,8,1]  ← 3 移到 5 前面
      摸 8: [3,5,8,1]  ← 8 比 5 大，不动
      摸 1: [1,3,5,8]  ← 1 移到最前面
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]           # 当前要插入的牌
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 比 key 大的往后移
            j -= 1
        arr[j + 1] = key        # key 插入空位
    return arr


# 演示
random.seed(42)
test_data = random.sample(range(100), 15)
print(f"\n原始数据: {test_data}")
print(f"冒泡结果: {bubble_sort(test_data)}")
print(f"插入结果: {insertion_sort(test_data)}")
print(f"Python  :  {sorted(test_data)}  ← 一行搞定，而且是 O(n log n)")


# ═══════════════════════════════════════════════════════════
# 第 4 部分：常见排序算法对比
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("常见排序算法速查")
print("=" * 60)
print("""
  算法          平均时间     最坏时间     空间      稳定？
  ──────        ───────     ───────     ─────     ────
  冒泡           O(n²)       O(n²)       O(1)      是
  插入           O(n²)       O(n²)       O(1)      是
  快速           O(n log n)  O(n²)       O(log n)  否
  归并           O(n log n)  O(n log n)  O(n)      是
  Timsort(Python) O(n log n) O(n log n)  O(n)      是

稳定 = 相等的元素保持原来的相对顺序（比如按姓名排序后，
        同名的人还是按原来的年龄顺序排列）。

面试不要背表，记住两点：
  - Python 的 sorted() 是 O(n log n)，最好的比较排序
  - 大多数情况下 O(n log n) 就是排序的天花板
""")


# ═══════════════════════════════════════════════════════════
# 练习
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 实现一个返回元素个数的函数 count_occurrences(arr, target)
# 在已排序的列表中用二分查找找到 target 的左右边界
# （提示：先找到最左边的 target，再找到最右边的 target）

print("练习 1: count_occurrences()")
# ↓↓↓



print("\n")

# ── 练习 2 ──
# 改写 bubble_sort，让它在每一轮后打印当前列表的样子
# 这样你能看到排序的过程

print("练习 2: bubble_sort 可视化版本")
# ↓↓↓



print("\n")

# ── 练习 3 ──
# 实现选择排序 (Selection Sort): 每轮找到最小的元素，和当前位置交换
# 提示: for i in range(n): 从 i 到末尾找最小值，和 i 交换

print("练习 3: selection_sort()")
# ↓↓↓



# ═══════════════════════════════════════════════════════════
# 复习练习（14-17：pandas 综合）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：对 sediment 的 TP 数据排序并找出前 3 和后 3")
print("用 pandas 读 WA.xlsx → 改列名 → 排 TP → 取前 3 和后 3 行")
print("=" * 50 + "\n")

# ↓↓↓



# ═══════════════════════════════════════════════════════════
# 就业前瞻：算法面试的真相
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】算法面试不是考你背代码")
print("=" * 50)
print("""
面试官问"写一个二分查找"，你写了 O(n) 的线性扫描 → 不通过。
面试官问"这个算法的时间复杂度是多少"，你答不上来 → 不通过。

但面试官不是在考你记忆力——他在考：
  1. 你知道不同数据结构和算法的特点吗？（选型能力）
  2. 你能估算代码的性能吗？（工程直觉）
  3. 你能用清晰的代码表达逻辑吗？（代码能力）

应对策略：
  1. LeetCode 刷 50 道高频题（从 Easy 开始）
  2. 每道题先自己想 15 分钟，做不出来再看答案
  3. 看完答案后关掉，自己重写一遍
  4. 写出时间复杂度和空间复杂度

你已经会的有:
  - 线性扫描 O(n)
  - 二分查找 O(log n)
  - 冒泡/插入排序 O(n²)
  - Python sorted O(n log n)

下一课（递归）学完，你的算法基础就能应对 80% 的面试问题了。
""")
