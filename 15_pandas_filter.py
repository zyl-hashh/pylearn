"""
Python 第 15 课 —— pandas 筛选与切片

相当于 Excel 的"筛选"功能，但写成代码。
以前你用 for + if 遍历列表筛选，现在一行搞定。
"""

import pandas as pd

# ── 加载数据 + 改短列名 ──
base = r"C:\Users\Nicholas\Desktop\赣江数据"
df = pd.read_excel(f"{base}/WA.xlsx", sheet_name="sediment")

# 列名是中文且有换行符，直接按位置改短名（最稳）
# 列 4='TP mg/kg'  列 12='pH'  列 14=粉砂  列 15=粘土
cols = list(df.columns)
cols[4] = "TP"
cols[12] = "pH"
cols[14] = "Silt"
cols[15] = "Clay"
df.columns = cols

print("改短名列名:", list(df.columns))
print(f"形状: {df.shape}\n")

# ═══════════════════════════════════════════════════════════
# 1. 布尔索引 — 最核心的筛选方式
# ═══════════════════════════════════════════════════════════

# df["列名"] > 值 → 返回一堆 True/False（布尔序列）
print("TP > 1000 的布尔序列:")
print((df["TP"] > 1000).head(10))

# 把布尔序列放进 df[...]，就只保留 True 的行：
high_tp = df[df["TP"] > 1000]
print(f"\nTP > 1000 的行数: {len(high_tp)} / {len(df)}")

# 多个条件：用 & (与) 和 | (或)，每个条件要加括号！
high_tp_low_silt = df[(df["TP"] > 1000) & (df["Silt"] > 60)]
#                     ↑ 括号            ↑ 括号
print(f"TP > 1000 且 Silt > 60: {len(high_tp_low_silt)} 行")

# 字符串条件
wa_rows = df[df["ID"].str.startswith("WA", na=False)]   # na=False = 空值按 False 处理
print(f"\nID 以 WA 开头: {len(wa_rows)} 行")
print(wa_rows["ID"].unique())                  # unique() = 去重看有哪些值

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. query() — 用字符串写条件（更直观，但列名不能有空格）
# ═══════════════════════════════════════════════════════════

result = df.query("TP > 1000 and Silt > 60")
print(f"query 方法结果: {len(result)} 行")
print(result[["ID", "TP", "Silt"]].head())
threshold = 1000
result2 = df.query("TP > @threshold")    # @变量名
print(f"TP > {threshold}: {len(result2)} 行")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 按列值筛选 — isin() 和 between()
# ═══════════════════════════════════════════════════════════

# 找特定样品
targets = ["WA1", "WA3", "WA5"]
wa_data = df[df["ID"].isin(targets)]
print(f"WA1/WA3/WA5 的数据:\n{wa_data[['ID', 'TP']]}")

# 数值范围筛选
mid_tp = df[df["TP"].between(900, 1100)]  # 900 <= TP <= 1100
print(f"\nTP 在 900-1100 之间: {len(mid_tp)} 行")
print(mid_tp[["ID", "TP"]].head())
print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 选择列 + 筛选行 — 一步到位
# ═══════════════════════════════════════════════════════════

# df.loc[行筛选, 列选择]
# 筛选 TP > 1000 的行，只要 ID、TP、Silt 三列
filtered = df.loc[df["TP"] > 1000, ["ID", "TP", "Silt"]]
print("TP > 1000 的样品:")
print(filtered.head(10))

# df.iloc[行位置, 列位置] — 按位置（不需要记列名）
subset = df.iloc[:5, [0, 4, 14, 15]]  # 前 5 行，第1/5/15/16 列
print(f"\niloc 按位置切片:\n{subset}")


# ═══════════════════════════════════════════════════════════
# 练习题（用上面改好列名的 df）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 筛选 pH < 7.0（偏酸性）的所有行
# 打印有多少行，以及前 5 行的 ID 和 pH

print("练习 1:")
# ↓↓↓
acidic = df[df['pH']<7]
print(f"pH < 7 的行数: {len(acidic)}")
print("前 5 行:\n", acidic[['ID','pH']].head(5))

print("\n")

# ── 练习 2 ──
# 筛选 ID 在 ["WA4", "WA5", "WA6"] 中，且 TP > 950 的行
# 打印这些行的 ID、TP、Silt 列

print("练习 2:")
# ↓↓↓
targets = ["WA4", "WA5", "WA6"]
result = df[df['ID'].isin(targets) & (df['TP']>950)]
print(result[['ID','TP','Silt']])

print("\n")

# ── 练习 3 ──
# 找出 Silt > 65 的样品中，TP 最高的那一行
# 提示：先筛选，再用 .sort_values("TP", ascending=False).head(1)

print("练习 3:")
# ↓↓↓
fa=df[df['Silt']>65]
faw=fa.sort_values('TP', ascending=False).head(1)
print(faw)


print("\n完成！下一步：16_pandas_groupby.py")
