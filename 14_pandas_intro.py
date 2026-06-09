"""
Python 第 14 课 —— pandas 入门：告别手动输数据

pandas 是 Python 里处理表格的库，相当于"代码版 Excel"。
之前你手动写 samples_raw = [{"name":"WA1", ...}]，
学会 pandas 后一行 pd.read_excel() 全搞定。

本节用你真实的 WA.xlsx 数据来演示。
"""

import pandas as pd

# ═══════════════════════════════════════════════════════════
# 1. 读 Excel — pd.read_excel()
# ═══════════════════════════════════════════════════════════

# 读一个 sheet
base = r"C:\Users\Nicholas\Desktop\赣江数据"
df = pd.read_excel(f"{base}/WA.xlsx", sheet_name="water")
# df = DataFrame（数据框），就是一张表格

# ═══════════════════════════════════════════════════════════
# 额外技巧：遇到乱糟糟的列名怎么办？
# ═══════════════════════════════════════════════════════════
# 有时候 Excel 里的列名是中文、有空格、有换行符——比如
# 'TP mg/kg'、'粉砂级<6\n3μm'。用 df.columns 看一看真实列名：
#   print(list(df.columns))
#
# 如果嫌列名太长/太乱，用 rename 改成短名：
#   df = df.rename(columns={"长列名": "短名", "TP mg/kg": "TP"})
#
# 或者直接按位置取：df.iloc[:, 4] = 第 5 列

# ═══════════════════════════════════════════════════════════
# 2. 看一眼数据 — 四个"偷看"函数
# ═══════════════════════════════════════════════════════════

print("前 5 行 (head)：")
print(df.head())           # 默认 5 行，df.head(10) 看 10 行

print(f"\n形状 (shape): {df.shape}")    # (行数, 列数)
print(f"列名 (columns): {list(df.columns)}")

print("\n信息 (info)：")
df.info()                  # 每列的数据类型、缺失值数量

print("\n统计摘要 (describe)：")
print(df.describe())       # count, mean, std, min, max... 只算数字列

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 取一列 — 两种方法
# ═══════════════════════════════════════════════════════════

# 方法 1: df["列名"]（推荐）
srp = df["SRP"]
print(f"SRP 列类型: {type(srp)}")       # Series（一维数组）
print(f"前 5 个 SRP 值:\n{srp.head()}")

# 方法 2: df.列名（列名不能有空格/中文时可以用）
# df.SRP   效果一样

# 取多列：df[["列1", "列2"]]
subset = df[["SRP", "TP"]].head(5)
print(f"\n取两列:\n{subset}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 取行 — iloc 和 loc
# ═══════════════════════════════════════════════════════════

# iloc = 按位置（你之前用的 .iloc[:8, 14] 就是这个）
print("iloc 前 3 行，前 2 列:")
print(df.iloc[:3, :2])

# loc = 按行标签（通常用不到，但要知道）
# df.loc[0:2, ["SRP", "TP"]]  → 行 0 到 2，列 SRP 和 TP

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 5. 直接转成你熟悉的字典列表
# ═══════════════════════════════════════════════════════════

# df.to_dict("records") = DataFrame → 字典列表
water_list = df.head(5).to_dict("records")
print("转成字典列表:")
for row in water_list:
    print(f"  {row}")

# 反过来：字典列表 → DataFrame
# pd.DataFrame(字典列表) ← 你综合项目里手动建的数据

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 6. 读所有 sheet 名
# ═══════════════════════════════════════════════════════════

xl = pd.ExcelFile(f"{base}/WA.xlsx")
print(f"WA.xlsx 里所有 sheet:")
for name in xl.sheet_names:
    print(f"  → {name}")

# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 读取 WA.xlsx 的 sediment sheet，打印它的 shape 和前 3 行

print("练习 1:")
# ↓↓↓
import pandas as pd
ba=r"C:\Users\Nicholas\Desktop\赣江数据"
df = pd.read_excel(f"{ba}/WA.xlsx",sheet_name="sediment")
print(df.shape)
print(df.head(3))


print("\n")

# ── 练习 2 ──
# 在上面读的 sediment 中，取第 14 和 15 列（粉砂和粘土）
# 打印它们的 describe() 统计摘要

print("练习 2:")
# ↓↓↓
df = pd.read_excel(f"{ba}/WA.xlsx",sheet_name="sediment")
print(df.iloc[ : ,14:16])
print(df.describe())


print("\n")

# ── 练习 3 ──
# 读 sediment 的前 8 行，转成字典列表
# 用循环打印 "样品: {ID}, 粉砂: {Silt}%"

print("练习 3:")
# ↓↓↓
sed_list= df.head(8).to_dict("records")
for s in sed_list:
    print(f"样品：{s['ID']}，粉砂：{s['粉砂（<6\n3μm）']}%")

print("\n完成！下一步：15_pandas_filter.py")
