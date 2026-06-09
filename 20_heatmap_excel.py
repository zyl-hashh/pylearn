"""
Python 第 20 课 —— 热力图 + 写入 Excel

热力图 = 矩阵数据的可视化（相关性矩阵、浓度分布）
写入 Excel = 用 pandas 把结果直接写到 .xlsx，不用 CSV 中转
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
out = os.path.expanduser("~/Desktop/python")

# ═══════════════════════════════════════════════════════════
# 1. 相关系数矩阵热力图
# ═══════════════════════════════════════════════════════════

# 模拟沉积物理化指标数据
np.random.seed(42)
df = pd.DataFrame({
    'TP': np.random.normal(1000, 80, 20),
    'Silt': np.random.normal(65, 8, 20),
    'Clay': np.random.normal(30, 5, 20),
    'OC': np.random.normal(12, 2, 20),
    'pH': np.random.normal(7.0, 0.3, 20),
})
corr = df.corr()   # 计算相关系数矩阵

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
#             ↑ 蓝-白-红色谱   ↑ 取值范围

# 标数值
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center',
                fontsize=11, color='black' if abs(corr.iloc[i,j]) < 0.7 else 'white')

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)
fig.colorbar(im, ax=ax, shrink=0.8, label='相关系数')
fig.tight_layout()
fig.savefig(f"{out}/lesson20_heatmap.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("热力图已保存")


# ═══════════════════════════════════════════════════════════
# 2. 写入 Excel — 比 CSV 强多了
# ═══════════════════════════════════════════════════════════

# 用真实数据做个简单的统计表
base = r"C:\Users\Nicholas\Desktop\赣江数据"
sed = pd.read_excel(f"{base}/WA.xlsx", sheet_name="sediment")
cols = list(sed.columns)
cols[4] = "TP"
cols[14] = "Silt"
cols[15] = "Clay"
sed.columns = cols

# 统计每个样品的 TP、Silt、Clay 均值
summary = sed.groupby("ID")[["TP", "Silt", "Clay"]].mean().head(8)

# 用 ExcelWriter 写入（支持多个 sheet！）
xlsx_path = f"{out}/lesson20_summary.xlsx"
with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
    summary.to_excel(writer, sheet_name='均值统计')
    sed.head(20).to_excel(writer, sheet_name='原始数据前20行')
    # 还能写更多 sheet...

print(f"Excel 已写入: {xlsx_path}")
print(f"  包含 sheet: 均值统计、原始数据前20行")


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 用上面 summary 的数据画热力图（TP/Silt/Clay 三个指标的相关性）

print("练习 1:")
# ↓↓↓
print("练习 1:")
# 计算相关系数矩阵
corr = summary.corr()
fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1)
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f'{corr.iloc[i, j]:.2f}', ha='center', va='center',
                fontsize=11, color='black' if abs(corr.iloc[i,j]) < 0.7 else 'white')
ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)
fig.colorbar(im, ax=ax, shrink=0.8, label='相关系数')
fig.tight_layout()
fig.savefig(f"{out}/exercise1_heatmap.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("练习 1 热力图已保存")

print("\n")

# ── 练习 2 ──
# 把上面 summary 写入 Excel，文件名 lesson20_my_summary.xlsx
# 注意不要往根目录写

print("练习 2:")
# ↓↓↓
xlsx_path = f"{out}/lesson20_my_summary.xlsx"
summary.to_excel(xlsx_path, sheet_name='均值统计',engine='openpyxl',index=False)
print(f"练习 2 Excel 已写入: {xlsx_path}")


# ═══════════════════════════════════════════════════════════
# 复习练习（06-07 课：异常处理 + 字符串）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：安全读文件 + 解析实验记录")
print("=" * 50 + "\n")

# 任务1：写 safe_read_file(path)，若文件不存在返回空字符串
# 任务2：给定一行 "WA5|34.95|0.8009|521.1"，用 split 解析并转成字典

# ↓↓↓ 你的代码 ↓↓↓
safe_read_file = lambda path: open(path, 'r', encoding='utf-8').read() if os.path.exists(path) else ""
print(safe_read_file("不存在的文件.txt"))  # 应该返回空字符串
record = "WA5|34.95|0.8009|521.1"
parts = record.split('|')
data_dict = {
    'ID': parts[0],
    'TP': float(parts[1]),
    'Silt': float(parts[2]),
    'Clay': float(parts[3])
}
print(data_dict)


# ═══════════════════════════════════════════════════════════
# 就业前瞻：Linux 是什么
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】Linux — 服务器都在跑的 OS")
print("=" * 50)
print("""
你用的 Windows 是桌面操作系统。Linux 是服务器操作系统——
你访问的网站、数据库、API，99% 跑在 Linux 上。

区别：
  Windows  → 图形界面，点鼠标，用 .exe
  Linux    → 命令行，敲键盘，用 .sh 脚本
  macOS    → 图形+命令行混合（底层和 Linux 同源）

学 Linux 对你来说最重要的是：
  1. 会连接远程服务器（ssh user@server）
  2. 会在 Linux 上跑 Python 脚本（和 Windows 一模一样）
  3. 会安装软件（apt install python3-pandas）

不用学桌面版 Linux，学命令行就够了。
你在 Git Bash 里打的 ls/cd/pwd 就是 Linux 命令——你已经在用了。

一句话：你的代码写完最终要部署到 Linux 服务器上跑。
""")
