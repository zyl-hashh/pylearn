"""
Python 入门第 9 课 —— 推导式进阶

以前你见过列表推导式: [x*2 for x in data]
现在学全套：列表、字典、集合推导式，以及嵌套推导式。
科研数据处理中一句话替代三行 for 循环。
"""

import math

# ═══════════════════════════════════════════════════════════
# 1. 列表推导式复习 + 条件筛选
# ═══════════════════════════════════════════════════════════

samples = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]
psi = [533.5, 517.6, 488.9, 475.1, 521.1, 467.5, 524.0, 539.6]
epc0 = [0.032, 0.045, 0.028, 0.051, 0.039, 0.047, 0.034, 0.041]

# 基础：对每个元素做一个变换
psi_kg = [p / 1000 for p in psi]          # mg/kg → g/kg
print(f"PSI (g/kg): {[f'{x:.3f}' for x in psi_kg]}")

# 加 if 条件 — 只取满足条件的
high_psi = [p for p in psi if p > 500]     # 只保留 PSI > 500 的
print(f"高 PSI (>500): {high_psi}")

# if/else — 三元表达式在推导式里
levels = ["高" if p > 520 else "中" if p > 480 else "低" for p in psi]
print(f"PSI 等级: {levels}")

# 多个列表配对
paired = [f"{n}: {p} mg/kg" for n, p in zip(samples, psi)]
print(f"配对: {paired[:3]}...")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 字典推导式
# ═══════════════════════════════════════════════════════════

# {键表达式: 值表达式 for 变量 in 可迭代对象}
# 从两个列表一键生成字典：
psi_dict = {name: value for name, value in zip(samples, psi)}
print(f"样品→PSI 字典: {psi_dict}")

# 加条件：只留高 PSI 的
high_dict = {n: p for n, p in zip(samples, psi) if p > 520}
print(f"高 PSI: {high_dict}")

# 从字典生成新字典（键值都变换）
squared = {n: round(p ** 0.5, 1) for n, p in psi_dict.items()}
print(f"PSI 开根号: {squared}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 嵌套推导式 — 处理多层数据
# ═══════════════════════════════════════════════════════════

# 二维数据：3 个样品 × 4 次重复测量
replicates = [
    [533.5, 528.1, 540.2, 531.9],   # WA1 的 4 次测量
    [517.6, 522.3, 514.8, 519.0],   # WA2
    [488.9, 485.5, 492.1, 490.3],   # WA3
]

# 所有测量值展平成一维
all_vals = [v for sample in replicates for v in sample]
print(f"展平: {all_vals}")

# 等价于：
# all_vals = []
# for sample in replicates:
#     for v in sample:
#         all_vals.append(v)

# 每个样品的平均值
means = [sum(sample) / len(sample) for sample in replicates]
print(f"平均值: {[f'{m:.1f}' for m in means]}")

# 找超过 530 的值并标记来源
high_finds = [(i + 1, v) for i, sample in enumerate(replicates)
              for v in sample if v > 530]
print(f"高于 530 的: {high_finds}")  # [(样品号, 值), ...]

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 集合推导式 — 去重
# ═══════════════════════════════════════════════════════════

# 和列表推导式一样，但用 {} 且元素唯一
depths = [0, 2, 4, 0, 2, 6, 4, 0, 2, 2]
unique_depths = {d for d in depths}
print(f"去重: {unique_depths}")

# 找出同样品在不同 sheet 都出现的 ID
sediment_ids = {"WA1", "WA2", "WA3", "WA4", "WA5"}
psi_ids = {"WA3", "WA4", "WA5", "WA6", "WA7", "WA8"}
# 交集
common = {s for s in sediment_ids if s in psi_ids}
print(f"两个 sheet 共同的: {common}")
# 或者直接用集合运算:
print(f"交集: {sediment_ids & psi_ids}")
print(f"只在 sediment: {sediment_ids - psi_ids}")
print(f"全部: {sediment_ids | psi_ids}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 5. 性能对比 — 为什么推导式更快
# ═══════════════════════════════════════════════════════════

# 推导式在 C 层面执行，比 for 循环 + append 快 30-50%
# 数据量大时区别明显
import time

n = 100000
start = time.time()
result1 = [i ** 2 for i in range(n)]
print(f"推导式: {time.time() - start:.7f} 秒")

start = time.time()
result2 = []
for i in range(n):
    result2.append(i ** 2)
print(f"for 循环: {time.time() - start:.7f} 秒")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 用列表推导式生成 1-20 中所有偶数的平方
# 输出: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
print([i**2 for i in range(2,21,2)])


print("\n")

# ── 练习 2 ──
# 用字典推导式，创建一个 {样品名: PSI值} 的字典，但只包含 PSI > 500 的
# 数据用上面 samples 和 psi 列表

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
dir = {n: v for n,v in zip(samples, psi) if v > 500}
print(dir)


print("\n")

# ── 练习 3 ──
# 给定嵌套列表 data = [[1,2,3], [4,5], [6,7,8,9]]
# 用嵌套推导式把所有数 ×10 然后展平成一个新列表
# 输出: [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
data = [[1,2,3], [4,5], [6,7,8,9]]
all_n = [v*10 for n in data for v in n]
print(all_n)


print("\n完成！下一步：10_sort_filter.py")
