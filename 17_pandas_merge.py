"""
Python 第 17 课 —— pandas 多表合并

你之前写吸附实验脚本，手动从 3 个 sheet 分别取数据，
再手动对齐 WA1-WA8。这节课学会后，一行 merge 搞定。

相当于 Excel 的 VLOOKUP，但快一万倍。
"""

import pandas as pd
import os

# ── 造演示数据（3 张表，各自缺失部分样品，模拟真实场景）──
wa_data = pd.DataFrame({
    "样品": ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"],
    "Depth": [0, 2, 4, 0, 2, 4, 0, 2],
    "TP": [980, 1020, 1100, 850, 920, 1080, 890, 950],
})

psi_data = pd.DataFrame({
    "样品": ["WA1", "WA2", "WA3", "WA5", "WA6", "WA8"],   # 缺 WA4, WA7
    "PSI": [533.5, 517.6, 488.9, 521.1, 467.5, 539.6],
})

qmax_data = pd.DataFrame({
    "样品": ["WA1", "WA2", "WA3", "WA4", "WA6", "WA7", "WA8"],  # 缺 WA5
    "Qmax": [0.623, 0.587, 0.541, 0.512, 0.503, 0.601, 0.635],
})

print("三张表:")
print(f"  wa:   {len(wa_data)} 行")
print(f"  psi:  {len(psi_data)} 行 (缺 WA4, WA7)")
print(f"  qmax: {len(qmax_data)} 行 (缺 WA5)")

# ═══════════════════════════════════════════════════════════
# 1. merge — 按共同列合并（最常用）
# ═══════════════════════════════════════════════════════════

# pd.merge(左表, 右表, on="共同列名", how="合并方式")

# how="inner" — 只保留两表都有的行（交集）
inner = pd.merge(wa_data, psi_data, on="样品", how="inner")
print(f"\ninner (交集): {len(inner)} 行 — 两表都有的样品")
print(inner)

# how="left" — 保留左表所有行，右表没有的填 NaN（最常用！）
left = pd.merge(wa_data, psi_data, on="样品", how="left")
print(f"\nleft (保留左表): {len(left)} 行 — WA4 和 WA7 的 PSI 显示 NaN")
print(left)

# how="outer" — 两表并集，缺失填 NaN
outer = pd.merge(psi_data, qmax_data, on="样品", how="outer")
print(f"\nouter (并集): {len(outer)} 行")
print(outer)

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 链式合并 — 三表合一
# ═══════════════════════════════════════════════════════════

# 先 psi merge qmax，结果再 merge wa
all_data = (
    wa_data
    .merge(psi_data, on="样品", how="left")
    .merge(qmax_data, on="样品", how="left")
)
print("三表合一 (left join):")
print(all_data)

# 完美对齐！三个 sheet 的数据在一张表里了

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 处理缺失值
# ═══════════════════════════════════════════════════════════

print("缺失值统计:")
print(all_data.isnull().sum())    # isnull() 返回 True/False, sum() 计数

# 方法 1: 删除有缺失的行
no_na = all_data.dropna()
print(f"\ndropna 后: {len(no_na)} 行（去掉了有 NaN 的行）")

# 方法 2: 填充缺失值
filled = all_data.fillna({"PSI": 0, "Qmax": 0})
print(f"\nfillna 填 0:\n{filled}")

# 方法 3: 填均值
psi_mean = all_data["PSI"].mean()
all_data_filled = all_data.fillna({"PSI": psi_mean})
print(f"\nPSI 缺失填均值 ({psi_mean:.1f}):")
print(all_data_filled)


# ═══════════════════════════════════════════════════════════
# 4. concat — 纵向拼接（上下堆）
# ═══════════════════════════════════════════════════════════

# merge 是横着拼（加列），concat 是竖着拼（加行）
df1 = pd.DataFrame({"样品": ["WA1", "WA2"], "值": [100, 200]})
df2 = pd.DataFrame({"样品": ["WA3", "WA4"], "值": [300, 400]})
stacked = pd.concat([df1, df2], ignore_index=True)   # ignore_index 重新编号
print(f"\nconcat 纵向拼接:\n{stacked}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 5. merge 速查表
# ═══════════════════════════════════════════════════════════
#
# how="inner"  → 交集（两表都有的才留）
# how="left"   → 保留左表全部（最常用）
# how="right"  → 保留右表全部
# how="outer"  → 并集（全留，缺失填 NaN）
#
# on="列名"    → 按这列合并（两表列名必须一样）
# left_on / right_on → 两表列名不一样时用


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 把 psi_data 和 qmax_data 用 outer 方式合并
# 然后 fillna({"PSI": 0, "Qmax": 0})
# 打印结果

print("练习 1:")
# ↓↓↓
outer = pd.merge(psi_data,qmax_data,on='样品',how='outer')
outer1=outer.fillna({'PSI':0,'Qmax':0})
print(outer1)


print("\n")

# ── 练习 2 ──
# 读吸附实验.xlsx 的 Qmax sheet 和 PSI sheet 的前 8 行
# 合并到一张表，打印合并后的行数和缺失值统计
# 提示：需要确保两表有一个共同的"样品名"列

print("练习 2:")
# ↓↓↓
from pathlib import Path
p=Path("C:/Users/Nicholas/Desktop/赣江数据/吸附实验/吸附实验.xlsx")
qmax=pd.read_excel(p,sheet_name='Qmax').head(8)
psi=pd.read_excel(p,sheet_name='PSI').head(8)
all_da=pd.merge(qmax,psi,on="ID",how='outer')
print(f'行数：{len(all_da)}，缺失列:{all_da.isnull().sum()}')


print("\n")

# ── 练习 3 ──
# 用 all_data（三表合一），筛选同时有 PSI 和 Qmax 的行
# 然后计算一列新数据 "ratio" = PSI * Qmax
# 打印样品名、PSI、Qmax、ratio，按 ratio 降序排列

print("练习 3:")
# ↓↓↓

new_data=all_data.dropna(subset=['PSI','Qmax'])
new_data['ratio']=new_data['PSI']*new_data['Qmax']
new_data_sorted=new_data.sort_values('ratio', ascending=False)
print("样品名、PSI、Qmax、ratio，按 ratio 降序排列:")
print(new_data_sorted[['样品','PSI','Qmax','ratio']])



print("\n完成！pandas 阶段结束。下一步：做复习题 review_01_10.py")
