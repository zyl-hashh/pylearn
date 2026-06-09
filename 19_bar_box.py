"""
Python 第 19 课 —— 柱状图与箱线图

柱状图 = 比较不同组的均值
箱线图 = 看数据分布（中位数、四分位数、异常值）
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
out = os.path.expanduser("~/Desktop/python")

# ═══════════════════════════════════════════════════════════
# 1. 柱状图 — 比较不同组
# ═══════════════════════════════════════════════════════════

sites = ['坝前', '坝中', '坝后']
tp_mean = [1050, 980, 890]
tp_std  = [45, 52, 38]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 基础柱状图
bars = ax1.bar(sites, tp_mean, color=['#2c7bb6', '#fdae61', '#d7191c'],
               edgecolor='white', linewidth=0.8)
ax1.set_ylabel('TP (mg/kg)')
ax1.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')

# 柱上标数值
for bar, val in zip(bars, tp_mean):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f'{val}', ha='center', fontsize=11)

# 带误差棒的柱状图
x = np.arange(len(sites))
ax2.bar(x, tp_mean, yerr=tp_std, capsize=5,      # yerr=误差线, capsize=帽子宽度
        color=['#2c7bb6', '#fdae61', '#d7191c'], edgecolor='white')
ax2.set_xticks(x)
ax2.set_xticklabels(sites)
ax2.set_ylabel('TP (mg/kg)')
ax2.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')

fig.tight_layout()
fig.savefig(f"{out}/lesson19_bar.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("柱状图已保存")

# ═══════════════════════════════════════════════════════════
# 2. 箱线图 — 看数据分布
# ═══════════════════════════════════════════════════════════

# 模拟三组重复测量数据
np.random.seed(42)
group_a = np.random.normal(1050, 40, 12)    # 均值1050 标准差40 12个数据点
group_b = np.random.normal(980, 55, 12)
group_c = np.random.normal(890, 35, 12)

fig, ax = plt.subplots(figsize=(8, 5))

bp = ax.boxplot([group_a, group_b, group_c],
                labels=['坝前', '坝中', '坝后'],
                patch_artist=True,       # 给箱体填色
                showmeans=True,           # 显示均值（绿色三角）
                meanprops=dict(marker='D', markerfacecolor='green', markersize=6))

# 箱体填色
for patch, color in zip(bp['boxes'], ['#2c7bb6', '#fdae61', '#d7191c']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_ylabel('TP (mg/kg)')
ax.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')

fig.tight_layout()
fig.savefig(f"{out}/lesson19_box.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("箱线图已保存")

# 箱线图怎么读：
#   箱子中间线 = 中位数
#   箱子上下边 = Q1(25%) 和 Q3(75%)
#   须线 = 非异常值范围
#   圆圈 = 异常值（超出 1.5 倍四分位距）
#   绿色菱形 = 均值


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 画一组柱状图：X轴 WA1-WA8，Y轴 PSI，带误差棒（误差自拟 8 个值）
# 柱体用单一颜色 '#2c7bb6'

print("练习 1:")
# ↓↓↓
site=['WA1','WA2','WA3','WA4','WA5','WA6','WA7','WA8']
psi=[321,422,347,368,389,356,411,357]
std=[21,15,34,42,26,35,44,29]
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(len(site))
fig,ax=plt.subplots(figsize=(7,5))
ax.bar(x,psi,yerr=std,capsize=5,color='#2c7bb6',edgecolor='white',linewidth=0.8)
ax.set_xticks(x)
ax.set_xticklabels(site)
ax.set_ylabel('PSI(mg/kg)')
ax.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')
fig.tight_layout()
fig.savefig(f"{out}/lesson19_1.tif",dpi=600,format='tiff',bbox_inches='tight',facecolor='white')
plt.close(fig)



print("\n")

# ── 练习 2 ──
# 用 boxplot 画两组数据：A组 = [520,535,510,545,528]、B组 = [480,495,470,510,488]
# 标签设为 'A组' 'B组'

print("练习 2:")
# ↓↓↓
import matplotlib.pyplot as plt
A组 = [520,535,510,545,528]
B组 = [480,495,470,510,488]
fig, ax=plt.subplots(figsize=(8,5))
bp=ax.boxplot([A组,B组],labels=['A组','B组'],
          patch_artist=True,       # 给箱体填色
          showmeans=True,           # 显示均值（绿色三角）
          meanprops=dict(marker='D', markerfacecolor='green', markersize=6))
for patch,color in zip(bp['boxes'],['#2c7bb6', '#fdae61']):
  patch.set_facecolor(color)
  patch.set_alpha(0.7)
ax.set_ylabel('y')
ax.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')

fig.tight_layout()
fig.savefig(f"{out}/lesson19_2.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)


# ═══════════════════════════════════════════════════════════
# 复习练习（04-05 课：字典 + 文件写入）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：把下面的样品字典列表写入 CSV")
print("=" * 50 + "\n")

data = [
    {"sample": "WA1", "TP": 996, "SRP": 0.035},
    {"sample": "WA2", "TP": 1096, "SRP": 0.042},
    {"sample": "WA3", "TP": 1154, "SRP": 0.038},
]

# ↓↓↓ 你的代码 ↓↓↓
import pandas as pd
from pathlib import Path
csv=Path.home()/'desktop/python/19.csv'
df=pd.DataFrame(data)
df.to_csv(csv,index=False)
print(f"已写入: {csv}")
# ═══════════════════════════════════════════════════════════
# 就业前瞻：终端 / 命令行
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】终端 — 不用鼠标操作电脑")
print("=" * 50)
print("""
程序员大部分时间在一个黑窗口里工作，叫"终端"（Terminal）。
你运行 python xxx.py 就是在用终端。

三个最基本的命令（打开你的 Git Bash 试试）：

  pwd          → 显示当前在哪个目录（Print Working Directory）
  ls           → 列出当前目录所有文件（LiSt）
  cd 文件夹名  → 进入那个文件夹（Change Directory）

动手试试：
  1. 打开 Git Bash（开始菜单搜 Git Bash）
  2. 输入 pwd，回车 —— 看到你当前在哪
  3. 输入 ls，回车 —— 看到桌面有哪些文件
  4. 输入 cd Desktop，回车 —— 进入桌面
  5. 输入 ls，回车 —— 和步骤 3 看到的不一样
  6. 输入 cd ..，回车 —— 返回上一级

这就是程序员"点开文件夹"的方式。没有鼠标，全用键盘。
""")
