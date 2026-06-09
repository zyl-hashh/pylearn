"""
Python 入门第 2 课 —— 列表与循环

列表 = 一排试管架，每个位置放一个数据
循环 = 对每个位置做同样的事

先跑一遍看效果，再去做最下面的练习题（要自己敲代码！）
"""

# ═══════════════════════════════════════════════════════════
# 1. 列表（list）— 用方括号 [] 装多个数据
# ═══════════════════════════════════════════════════════════

# 你之前代码里的 samples = ['WA1','WA2',...] 就是列表
samples = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]

# 用下标取元素（注意！Python 从 0 开始数）
print("第 1 个元素:", samples[0])   # WA1
print("第 3 个元素:", samples[2])   # WA3
print("最后 1 个:", samples[-1])    # WA8（负数 = 从右边数）

# 取一段（切片）— 用冒号
print("前 3 个:", samples[:3])      # WA1, WA2, WA3（不含下标3）
print("第 4-6 个:", samples[3:6])   # WA4, WA5, WA6

# 列表里可以放数字
psi_values = [533.5, 517.6, 488.9, 475.1, 521.1, 467.5, 524.0, 539.6]
print(f"PSI 列表有 {len(psi_values)} 个值")  # len() = 列表长度
print(f"最大值: {max(psi_values)}")
print(f"最小值: {min(psi_values)}")
print(f"总和: {sum(psi_values)}")
print(f"平均值: {sum(psi_values) / len(psi_values):.1f}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. for 循环 — 逐个处理列表里的东西
# ═══════════════════════════════════════════════════════════

# 形式 1：直接拿元素
print("逐个打印样品名：")
for name in samples:       # 每次循环 name 变成列表的下一个元素
    print(f"  样品: {name}")

# 形式 2：需要序号时用 enumerate
print("\n带序号的打印：")
for i, name in enumerate(samples):   # i = 序号, name = 元素
    print(f"  第 {i+1} 个: {name}")

# 形式 3：需要同时遍历两个列表用 zip
print("\n样品和 PSI 值配对：")
for name, psi in zip(samples, psi_values):
    print(f"  {name}: PSI = {psi} mg/kg")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. range() — 生成一串数字
# ═══════════════════════════════════════════════════════════

# range(8) = 0, 1, 2, 3, 4, 5, 6, 7
print("range(8):")
for i in range(8):
    print(f"  i = {i}")

# 这在画图时用来自动生成 X 轴位置
import numpy as np
x_positions = np.arange(len(samples))  # np.arange(8) = [0,1,2,3,4,5,6,7]
print(f"\nX 轴位置: {x_positions}")


# ═══════════════════════════════════════════════════════════
# 4. 列表推导式 — 一行写完循环
# ═══════════════════════════════════════════════════════════
# 你之前 Qmax 脚本里见过： [float(v) for v in raw_data]
# 翻译成人话：for v in raw_data → 每个 v 都 float(v) → 装进新列表

# 普通写法：
squares_normal = []
for i in range(5):
    squares_normal.append(i ** 2)    # append = 往列表末尾加一个元素
print("普通写法:", squares_normal)

# 推导式写法（一行搞定）：
squares = [i ** 2 for i in range(5)]
print("推导式写法:", squares)


# ═══════════════════════════════════════════════════════════
# 练习题（必须自己敲代码，不要复制粘贴！）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题 — 在下面空白处自己写代码")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 已知 8 个样品的 EPC0 值（mg/L）：
epc0 = [0.032, 0.045, 0.028, 0.051, 0.039, 0.047, 0.034, 0.041]
# 要求：用 for 循环逐个打印 "样品 X: EPC0 = Y mg/L"，X 是序号（1-8），Y 是对应值

print("练习 1:")
# ↓↓↓ 在下面写你的代码 ↓↓↓

for i,value in enumerate(epc0):
    print(f"样品 {i+1}： EPC0 = {value} mg/L")


# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n")

# ── 练习 2 ──
# 已知上面 epc0 列表和 8 个样品对应的 SRP 值：
srp = [0.045, 0.052, 0.038, 0.061, 0.044, 0.055, 0.041, 0.049]
# 要求：用列表推导式创建一个新列表 diff，每个元素 = srp[i] - epc0[i]
# 然后打印 diff 列表
# 提示：用 zip()

print("练习 2:")
# ↓↓↓ 在下面写你的代码 ↓↓↓
diff=[epc0_val-psi_val for epc0_val,psi_val in zip(epc0, srp)]
print(diff)



# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n")

# ── 练习 3 ──
# 已知 Qmax 值（单位 mg/g）：
qmax = [0.623, 0.587, 0.541, 0.512, 0.598, 0.503, 0.601, 0.635]
# 要求：找出 Qmax > 0.6 的样品（名字用上面的 samples 列表）
# 提示：用 for + zip + if

print("练习 3:")
# ↓↓↓ 在下面写你的代码 ↓↓↓
high_qmax_samples = [name for name,q in zip(samples,qmax) if q>0.6]


# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n完成！下一步：03_conditions_functions.py")
