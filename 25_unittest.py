"""
Python 第 25 课 —— 单元测试

以前你"测试"代码的方法：跑一遍，肉眼看输出对不对。
单元测试 = 用代码测试代码，自动判断对错。

你以后找工作面试，面试官会问"你写过测试吗"——这节课就是答案。
"""

import math

# ═══════════════════════════════════════════════════════════
# 1. assert — 最简测试（一行搞定）
# ═══════════════════════════════════════════════════════════

def calc_Q(C0, Ce, V, m):
    return (C0 - Ce) * V / m

# assert 条件, "失败时的提示"
# 条件为 True 啥事没有，False 直接报错
assert calc_Q(75, 33.76, 0.020, 1) == 0.8248, "WA1 Q 值不对"
assert abs(calc_Q(75, 34.85, 0.020, 1) - 0.803) < 0.001, "WA2 Q 值偏差过大"
#         ↑ 浮点数用近似比较，不直接用 ==

print("基础 assert 测试通过")

# 如果 assert 失败会怎样？取消下面注释试试：
assert calc_Q(75, 33.76, 0.020, 1) == 999, "故意写错的预期"


# ═══════════════════════════════════════════════════════════
# 2. 用 if/raise 做数据验证（你已经在做了）
# ═══════════════════════════════════════════════════════════

def calc_PSI(Q_mg_g, Ce):
    """计算 PSI，附带输入验证"""
    if Q_mg_g <= 0:
        raise ValueError(f"Q 必须 > 0，实际 {Q_mg_g}")
    if Ce <= 1:
        raise ValueError(f"Ce 必须 > 1（log10(≤1) 无效），实际 {Ce}")
    return Q_mg_g * 1000 / math.log10(Ce)

# 验证正常情况
result = calc_PSI(0.823, 34.11)
assert result > 500, f"PSI 应该 > 500，实际 {result}"
print(f"PSI 计算通过: {result:.1f}")

# 验证异常输入 会 抛出异常（用 try 接住）
try:
    calc_PSI(-1, 34.11)
    print("❌ 没抛异常！")
except ValueError:
    print("✅ 负数输入正确抛出异常")

try:
    calc_PSI(0.823, 0.5)
    print("❌ 没抛异常！")
except ValueError:
    print("✅ Ce <= 1 正确抛出异常")


# ═══════════════════════════════════════════════════════════
# 3. unittest 框架 — 专业写法
# ═══════════════════════════════════════════════════════════

import unittest

class TestPhosphorus(unittest.TestCase):
    """测磷计算相关函数"""

    def test_calc_Q_normal(self):
        """正常输入"""
        result = calc_Q(75, 33.76, 0.020, 1)
        self.assertAlmostEqual(result, 0.8248, places=4)

    def test_calc_Q_zero_diff(self):
        """Ce = C0 时 Q 应为 0"""
        result = calc_Q(75, 75, 0.020, 1)
        self.assertEqual(result, 0.0)

    def test_calc_PSI_typical(self):
        """典型 PSI 值"""
        result = calc_PSI(0.823, 34.11)
        self.assertGreater(result, 500)

    def test_calc_PSI_raises_on_negative_Q(self):
        """负数 Q 应抛异常"""
        with self.assertRaises(ValueError):
            calc_PSI(-1, 34.11)

    def test_calc_PSI_raises_on_small_Ce(self):
        """Ce <= 1 应抛异常"""
        with self.assertRaises(ValueError):
            calc_PSI(0.823, 0.5)

# 运行测试
# 实际项目里把下面这行放在 if __name__ == "__main__": 里
# unittest.main()

print("\n所有测试通过！（用 unittest 框架的话还要加一行 unittest.main()）")


# ═══════════════════════════════════════════════════════════
# 4. 测试原则
# ═══════════════════════════════════════════════════════════

print("""
测试三原则：
  1. 测正常情况 → 输入合理数据，输出应在预期范围
  2. 测边界情况 → Ce=0, Ce=C0, Ce=负数
  3. 测异常情况 → 输入不合法时是否抛出异常

面试回答模板：
  "我会用 assert 做快速验证，用 unittest 框架写正式的
   测试用例，确保代码修改后核心计算逻辑不会坏。"
""")


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 写一个函数 safe_divide(a, b)，b=0 时返回 None
# 用 assert 测试: safe_divide(10, 2)==5, safe_divide(10, 0) is None

print("练习 1:")
# ↓↓↓
def safe_divide(a,b):
    if b==0:
        return None
    return a/b
assert safe_divide(10, 2)==5,"没有问题"
assert safe_divide(10, 0)==None,"不能为0"


print("\n")

# ── 练习 2 ──
# 写一个 unittest.TestCase，包含至少 2 个测试方法

print("练习 2:")
# ↓↓↓
import unittest
class Testone(unittest.TestCase):
    def test_1(self):
        b=9-2
        self.assertEqual(b,7)
    def test_2(self):
        b=5*5
        self.assertGreater(b,24)
    def test_3(self):
        with self.assertRaises(ValueError):
            raise ValueError("这是一个错误")
if __name__ == "__main__":
    unittest.main()

# ═══════════════════════════════════════════════════════════
# 复习练习：综合项目重写
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：用 pandas 替代手动字典，重写 PSI 计算")
print("""
任务：
  1. 用 pandas 创建 DataFrame（Ce 数据同上 8 个样品）
  2. 用 apply() 计算 Q 和 PSI 列
  3. 按 PSI 降序排列
  4. 输出到 Excel
""")
print("=" * 50 + "\n")

# ↓↓↓ 你的代码 ↓↓↓
import pandas as pd
import math
from pathlib import Path
df=pd.DataFrame({"样品": ["WA1","WA2","WA3","WA4","WA5","WA6","WA7","WA8"],
    "Ce": [33.76, 34.85, 36.84, 37.73, 34.95, 38.03, 35.85, 34.46]})
C0, V, m = 75.0, 0.020, 1.0
df['Q']=df['Ce'].apply(lambda ce:(C0-ce)*V/m)
df['PSI']=df['Ce'].apply(lambda ce:(C0-ce)*V/m*1000/math.log10(ce))
df=df.sort_values(['PSI'],ascending=False)
out=Path.home()/'Desktop'/'python'/'PSI.xlsx'
df.to_excel(out,index=False)


# ═══════════════════════════════════════════════════════════
# 就业前瞻：面试会问什么
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】数据结构 — 面试必问")
print("=" * 50)
print("""
你学会的数据类型，在计算机科学里有正式名称。

  你会用的              专业名称        面试常问
  ─────────            ────────        ─────────
  list 列表             数组 Array      如何反转？找最大？
  dict 字典             哈希表 Hash     为什么查得快？O(1) 什么意思？
  for + if              遍历/搜索       O(n) 什么意思？
  递归（还没学）         递归 Recursion  斐波那契数列

面试官问"你知道什么数据结构"时，你可以说：

  "我日常用 Python 的 list 和 dict 做数据处理。
   list 适合有序存储和遍历，dict 适合键值查找，
   在科研数据处理中 dict 的查找效率比 list 高很多，
   因为它是 O(1) 而 list 是 O(n)。"

这比 90% 的科班应届生都答得好——因为他们只会背书，
而你用真实科研场景解释了为什么。

关于 O(1) 和 O(n)（记个概念就行）：
  在 list 里找一样东西 → 最多要把整个 list 翻一遍 → O(n)
  在 dict 里找一样东西 → 一次就找到了 → O(1)
  这就是为什么 dict 比 list 快。

25 节课全部完成！你已经从业余选手走到了能写出能被面试官认可的代码。
""")
