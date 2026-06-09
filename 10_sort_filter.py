"""
Python 入门第 10 课 —— 排序与过滤

科研数据处理两大高频操作：
  排序：哪个样品 PSI 最高？按 EPC0 从小到大排列？
  过滤：筛选 Qmax > 0.6 的数据、去掉异常值

这节课用你真实的数据结构（字典列表）来练。
"""

# ═══════════════════════════════════════════════════════════
# 1. sorted() — 万能排序函数
# ═══════════════════════════════════════════════════════════

samples = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623, "EPC0": 0.032},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587, "EPC0": 0.045},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541, "EPC0": 0.028},
    {"name": "WA4", "PSI": 475.1, "Qmax": 0.512, "EPC0": 0.051},
    {"name": "WA5", "PSI": 521.1, "Qmax": 0.598, "EPC0": 0.039},
    {"name": "WA6", "PSI": 467.5, "Qmax": 0.503, "EPC0": 0.047},
    {"name": "WA7", "PSI": 524.0, "Qmax": 0.601, "EPC0": 0.034},
    {"name": "WA8", "PSI": 539.6, "Qmax": 0.635, "EPC0": 0.041},
]

# 对简单列表排序
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"升序: {sorted(numbers)}")             # [1, 1, 2, 3, 4, 5, 9]
print(f"降序: {sorted(numbers, reverse=True)}") # [9, 5, 4, 3, 2, 1, 1]

# 对字典列表排序 — 用 key= 指定按哪个字段
by_psi = sorted(samples, key=lambda s: s["PSI"])
print(f"\n按 PSI 升序:")
for s in by_psi:
    print(f"  {s['name']}: PSI={s['PSI']}")

by_qmax_desc = sorted(samples, key=lambda s: s["Qmax"], reverse=True)
print(f"\n按 Qmax 降序:")
for s in by_qmax_desc:
    print(f"  {s['name']}: Qmax={s['Qmax']}")

# lambda s: s["PSI"] 的意思是：
#   对每个元素 s，返回 s["PSI"] 作为排序依据
#   等于定义了一个临时函数

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 多级排序 — 先按 A 排，A 相同按 B 排
# ═══════════════════════════════════════════════════════════

# 用元组 (字段1, 字段2)
complex_data = [
    {"site": "坝前", "depth": 2, "TP": 1050},
    {"site": "坝前", "depth": 0, "TP": 980},
    {"site": "坝前", "depth": 4, "TP": 1100},
    {"site": "坝后", "depth": 0, "TP": 850},
    {"site": "坝后", "depth": 2, "TP": 920},
]

sorted_complex = sorted(complex_data, key=lambda d: (d["site"], d["depth"]))
print("先按位置再按深度:")
for d in sorted_complex:
    print(f"  {d['site']}  {d['depth']}cm  TP={d['TP']}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. filter() — 筛选
# ═══════════════════════════════════════════════════════════

# filter(判断函数, 可迭代对象) → 只留下判断为 True 的元素

# 方法 1：filter + lambda 
high_epc0 = list(filter(lambda s: s["EPC0"] > 0.04, samples))
print(f"EPC0 > 0.04 的样品:")
for s in high_epc0:
    print(f"  {s['name']}: EPC0={s['EPC0']}")

# 方法 2：列表推导式（很多人觉得更可读，效果一样）
high_epc0_v2 = [s for s in samples if s["EPC0"] > 0.04]

# 两者完全等价，选你喜欢的
print("(或直接用推导式写)")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 筛掉异常值（科研必备技能）
# ═══════════════════════════════════════════════════════════

# 简单的统计学方法：超过 2σ 算异常
numbers = [533.5, 517.6, 488.9, 475.1, 521.1, 467.5, 524.0, 539.6, 999.0]
#                                                              ↑ 这个明显异常

mean = sum(numbers) / len(numbers)
# 计算标准差
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std = variance ** 0.5

print(f"均值: {mean:.1f}, 标准差: {std:.1f}")
print(f"正常范围: [{mean - 2*std:.1f}, {mean + 2*std:.1f}]")

clean = [x for x in numbers if abs(x - mean) <= 2 * std]
print(f"过滤前: {numbers}")
print(f"过滤后: {clean}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 5. 排名 — 给每个样品一个名次
# ═══════════════════════════════════════════════════════════

# enumerate(sorted(...)) 生成排名
ranked = sorted(samples, key=lambda s: s["PSI"], reverse=True)

print("PSI 排名：")
for rank, s in enumerate(ranked, start=1):   # start=1 让序号从 1 开始
    print(f"  {rank}. {s['name']}: {s['PSI']} mg/kg")

# 把排名写回字典
for rank, s in enumerate(ranked, start=1):
    s["PSI_rank"] = rank

print(f"\nWA3 的 PSI 排名: {next(s for s in ranked if s['name']=='WA3')['PSI_rank']}")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# 数据：
measurements = [
    {"sample": "S1", "pH": 7.2, "DO": 8.5, "TP": 0.12},
    {"sample": "S2", "pH": 6.8, "DO": 7.1, "TP": 0.35},
    {"sample": "S3", "pH": 7.5, "DO": 9.2, "TP": 0.08},
    {"sample": "S4", "pH": 7.1, "DO": 6.3, "TP": 0.42},
    {"sample": "S5", "pH": 8.2, "DO": 8.9, "TP": 0.05},
]

# ── 练习 1 ──
# 按 TP 升序排列 measurements，打印 "样品 X: TP=Y"

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
mea= sorted(measurements, key=lambda s:s['TP'])
for m in mea:
    print(f"样品 {m['sample']}: TP={m["TP"]}")


print("\n")

# ── 练习 2 ──
# 筛选 DO > 8.0 且 pH < 8.0 的样品
# 打印它们的名字和 DO、pH

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
mea1 = [s for s in measurements if s['DO']>8 and s['pH']<8]
for m in mea1:
    print(f"{m['sample']}: DO={m['DO']},pH={m['pH']}")


print("\n")

# ── 练习 3 ──
# 给 measurements 按 TP 升序排名（1=最低TP），名次存到 "TP_rank" 键
# 注意：TP 最低 = 水质最好 = 第 1 名

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
mea2=sorted(measurements, key=lambda m: m['TP'])
for i,n in enumerate(mea2,start=1):
    n['TP_rank'] =i
for n in mea2:
    print(f"{n['TP_rank']} .TP = {n['TP']}")


print("\n完成！前 10 节学完了。下一步进入 pandas 阶段（14-17 节）。")
print("中间 11-13 节（lambda/模块/虚拟环境）是过渡内容，等你需要时再给。")
