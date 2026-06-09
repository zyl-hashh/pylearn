"""
Python 第 18 课 —— matplotlib 子图布局

一张图放多个坐标轴，拼成论文里的多面板图（a/b/c/d）。
之前你画的图都是单面板，这节课学会 subplots 布局。
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# 中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.expanduser("~/Desktop/python")

# ═══════════════════════════════════════════════════════════
# 1. plt.subplots(行, 列) — 创建多面板
# ═══════════════════════════════════════════════════════════

x = np.arange(1, 9)
psi = [533.5, 517.6, 488.9, 475.1, 521.1, 467.5, 524.0, 539.6]
qmax = [0.623, 0.587, 0.541, 0.512, 0.598, 0.503, 0.601, 0.635]
epc0 = [0.032, 0.045, 0.028, 0.051, 0.039, 0.047, 0.034, 0.041]

# 1 行 2 列 = 两个并排的图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
#       ↑ ax1 是左图，ax2 是右图（元组解包）

# 左图
ax1.plot(x, psi, 'o-', color='#2c7bb6', linewidth=2, markersize=8)
ax1.set_xlabel('样品序号')
ax1.set_ylabel('PSI (mg/kg)')
ax1.grid(True, linestyle='--', color='lightgray', alpha=0.7)
ax1.set_title('PSI', fontsize=12)   # 子图可以有标题

# 右图
ax2.bar(x, qmax, color='#d7191c', alpha=0.8)
ax2.set_xlabel('样品序号')
ax2.set_ylabel('Qmax (mg/g)')
ax2.grid(True, linestyle='--', color='lightgray', alpha=0.7, axis='y')  # 只要Y轴网格
ax2.set_title('Qmax', fontsize=12)

fig.tight_layout()
fig.savefig(f"{output_dir}/lesson18_1x2.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("1×2 面板已保存")

# ═══════════════════════════════════════════════════════════
# 2. 2 行 2 列 — 经典论文四面板
# ═══════════════════════════════════════════════════════════

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# axes 是二维数组: axes[0][0], axes[0][1], axes[1][0], axes[1][1]

titles = ['PSI', 'Qmax', 'EPC0', 'EPC0 vs PSI']
data_list = [psi, qmax, epc0, None]

for idx, ax in enumerate(axes.flat):   # .flat 把二维展平成一行
    if idx < 3:
        ax.bar(x, data_list[idx], color=['#2c7bb6', "#E61C20", '#fdae61'][idx])
        ax.set_title(titles[idx])
    else:
        # 第四格画散点
        ax.scatter(epc0, psi, c='#2c7bb6', s=60)
        ax.set_xlabel('EPC0 (mg/L)')
        ax.set_ylabel('PSI (mg/kg)')
        ax.set_title(titles[idx])
    ax.grid(True, linestyle='--', color='lightgray', alpha=0.7)

fig.tight_layout()
fig.savefig(f"{output_dir}/lesson18_2x2.tif", dpi=600, format='tiff',
            bbox_inches='tight', facecolor='white')
plt.close(fig)
print("2×2 面板已保存")


# ═══════════════════════════════════════════════════════════
# 练习题（主课）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 用 subplots(2, 1) 画两张上下堆叠的图：上图 PSI 折线，下图 Qmax 柱状
# 每张图加网格

print("练习 1:")
# ↓↓↓
import matplotlib.pyplot as plt
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(5,8))
ax1.plot(x,psi,'-o',color='red',linewidth=2,markersize=8,alpha=0.7)
ax1.set_xlabel('site')
ax1.set_ylabel('PSI(mg/kg)')
ax1.set_title('PSI')
ax1.grid(True,color='lightgray',linestyle='--',alpha=0.5)
ax2.bar(x,qmax,color='blue',alpha=0.8)
ax2.set_xlabel('site')
ax2.set_ylabel('Qmax(mg/kg)')
ax2.set_title('Qmax')
ax2.grid(True,color='lightgray',linestyle='--',alpha=0.5,axis='y')
fig.tight_layout()
fig.savefig(f"{output_dir}/lesson18_2×1.tif",dpi=600,format='tif',bbox_inches='tight',facecolor='white')


print("\n（检查 lesson18_2x1.tif）")


# ═══════════════════════════════════════════════════════════
# 复习练习（02-03 课：循环 + 函数）
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("复习练习：写一个函数 calc_removal_rate(C0, Ce)")
print("返回去除率 = (C0-Ce)/C0*100，然后用循环批量算 8 个样品")
print("=" * 50 + "\n")

ce_vals = [33.76, 34.85, 36.84, 37.73, 34.95, 38.03, 35.85, 34.46]

# ↓↓↓ 你的代码 ↓↓↓
def cacl_removal_rate(C0,Ce):
    return ((C0-Ce)/C0)*100
C0=75
for s in ce_vals:
    print(f"去除率={cacl_removal_rate(C0,s):.2f}%")


# ═══════════════════════════════════════════════════════════
# 就业前瞻：Git 是什么
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("【就业前瞻】Git — 程序员的时间机器")
print("=" * 50)
print("""
你写论文是不是这样：
  论文_v1.docx → 论文_v2.docx → 论文_最终版.docx → 论文_真的最终.docx

Git 就是解决这个问题的。它不是保存多个副本，而是记录每一次修改的"快照"。
你可以随时回到三天前的版本，也可以看谁改了哪一行。

三个核心概念（记住就行，不用会）：

  仓库 (repo)   = 一个项目的"档案馆"
  提交 (commit) = 一次"拍照"，记录当前所有文件的样子
  分支 (branch) = 一条"平行时间线"，用来试验新功能不破坏主版本

你以后会学到：
  git init       → 把当前文件夹变成仓库
  git add .      → 把修改加入暂存区
  git commit -m "修复了PSI计算bug"  → 拍照保存
  git log        → 看历史快照

今天不做操作，只记住一句话：
  "Git 是你写代码时的 Ctrl+Z，但是能看到十年前的那一步"

下一步：19_bar_box.py
""")
