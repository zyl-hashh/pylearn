"""
Python 第 16 课 —— pandas 分组统计 groupby

相当于 Excel 的"数据透视表"。
以前你手动建字典统计，现在一句 groupby 搞定。

本节用真实的 sediment 数据（已改短列名）。
"""

import pandas as pd

# ── 加载数据 + 改短列名 ──
base = r"C:\Users\Nicholas\Desktop\赣江数据"
df = pd.read_excel(f"{base}/WA.xlsx", sheet_name="sediment")

# 按位置改短名列（列名是中文有换行符，直接字符串匹配不稳定）
cols = list(df.columns)
cols[4] = "TP"
cols[12] = "pH"
cols[14] = "Silt"
cols[15] = "Clay"
df.columns = cols

# 加一列"类型"用于分组练习：WA1-WA4→坝前，WA5-WA8→坝后
def assign_zone(name):
    if name in ["WA1", "WA2", "WA3", "WA4"]:
        return "坝前"
    else:
        return "坝后"

df["Zone"] = df["ID"].apply(assign_zone)  # apply = 对每个 ID 调用函数

print(f"数据: {df.shape[0]} 行")
print(f"新增 Zone 列: {df[['ID', 'Zone', 'TP']].head(8)}\n")

# ═══════════════════════════════════════════════════════════
# 1. 基本分组 — groupby + 聚合
# ═══════════════════════════════════════════════════════════

# 按 Zone 分组，求 TP 均值
zone_tp = df.groupby("Zone")["TP"].mean()
print("按 Zone 分组，TP 均值:")
print(zone_tp)
print()

# 一次算多个统计量
zone_stats = df.groupby("Zone")["TP"].agg(["mean", "std", "min", "max", "count"])
print("一组多指标:")
print(zone_stats)

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 多列同时统计
# ═══════════════════════════════════════════════════════════

# 同时统计多列
multi = df.groupby("Zone")[["TP", "Silt", "Clay"]].mean()
print("多列均值:")
print(multi)

# 不同列用不同统计方法
custom = df.groupby("Zone").agg({
    "TP": "mean",
    "Silt": ["mean", "std"],
    "ID": "count",          # 每组的行数
})
print(f"\n不同列不同统计:\n{custom}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 多级分组（按两个列）
# ═══════════════════════════════════════════════════════════

# 先按 Zone，再在每个 Zone 内按 pH 范围分组
# 先加一列 pH 等级
df["pH_level"] = df["pH"].apply(lambda x: "偏酸" if x < 7.0 else "中性/偏碱")

multi_group = df.groupby(["Zone", "pH_level"])["TP"].mean()
print("双级分组 (Zone × pH):")
print(multi_group)

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. transform — 分组后保持原行数
# ═══════════════════════════════════════════════════════════

# groupby().mean() 把数据压缩到每组一行
# groupby().transform("mean") 保持原来的行数，每行填本组均值

df["TP_zone_mean"] = df.groupby("Zone")["TP"].transform("mean")
print("加一列'该 Zone 的 TP 均值'（原行数不变）:")
print(df[["ID", "Zone", "TP", "TP_zone_mean"]].head(8))

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 5. 排序 — 把分组结果整理清楚
# ═══════════════════════════════════════════════════════════

# 按 TP 降序看前几名
sorted_df = df.sort_values("TP", ascending=False)
print("TP 最高 5 行:")
print(sorted_df[["ID", "TP", "Silt", "Zone"]].head(5))

# 分组后再排序
zone_mean = df.groupby("Zone")["TP"].mean()
print(zone_mean)
zone_sorted = zone_mean.sort_values(ascending=False)
print(f"\nZone TP 均值排序:\n{zone_sorted}")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 按 Zone 分组，计算 Silt 和 Clay 的均值

print("练习 1:")
# ↓↓↓
sc = df.groupby(['Zone'])[['Silt','Clay']].mean()
print(sc)


print("\n")

# ── 练习 2 ──
# 按 pH_level 分组，统计每组有多少个样品（count），以及 TP 的 mean 和 std

print("练习 2:")
# ↓↓↓
ph_stats = df.groupby('pH_level').agg({'ID':'count','TP':['mean','std']})
print(ph_stats)



print("\n")

# ── 练习 3 ──
# 用 transform 给每个样品加一列 "Silt_zone_mean"
# 然后计算每行 Silt 与其所在 Zone 均值的偏差: df["Silt_deviation"] = df["Silt"] - df["Silt_zone_mean"]
# 打印 ID、Zone、Silt、Silt_zone_mean、Silt_deviation 前 8 行

print("练习 3:")
# ↓↓↓
df['Silt_zone_mean']= df.groupby(['Zone'])['Silt'].transform('mean')
df["Silt_deviation"] = df["Silt"] - df["Silt_zone_mean"]
print(df[['ID','Zone','Silt','Silt_zone_mean','Silt_deviation']].head(8))


print("\n完成！下一步：17_pandas_merge.py")
