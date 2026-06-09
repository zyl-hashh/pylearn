"""
第 1-10 课复习卷（共 10 题，覆盖基础阶段全部知识点）

规则：
  1. 关掉答案文件 answers_01_10.py
  2. 每道题独立写，不限时间
  3. 做完一题跑一次，看到正确输出再做下一题
  4. 10 题全部独立完成 = 基础阶段毕业
"""

import math
from pathlib import Path

print("=" * 50)
print("Python 基础阶段复习卷")
print("=" * 50)

# ═══════════════════════════════════════════════════════════
# 第 1 题 — 变量与 f-string（01 课）
# ═══════════════════════════════════════════════════════════
# 已知样品 WA3 的初始磷浓度 C0=75 mg/L，平衡浓度 Ce=36.84 mg/L
# 用 f-string 打印: "WA3: C0=75.0 mg/L, Ce=36.8 mg/L, 去除率=50.9%"
# 去除率 = (C0 - Ce) / C0 × 100，保留 1 位小数

print("\n第 1 题:")


# ↓↓↓ 你的代码 ↓↓↓
C0=75
Ce=36.84
print(f"WA3: C0=75.0 mg/L, Ce=36.8 mg/L, 去除率={((C0 - Ce) / C0 * 100):.1f}%")


# ═══════════════════════════════════════════════════════════
# 第 2 题 — 列表与循环（02 课）
# ═══════════════════════════════════════════════════════════
# 已知 EPC0 列表，打印所有 EPC0 > 0.04 的值，格式: "EPC0=0.045 > 0.04"

print("\n第 2 题:")
epc0_list = [0.032, 0.045, 0.028, 0.051, 0.039, 0.047, 0.034, 0.041]


# ↓↓↓ 你的代码 ↓↓↓
for s in epc0_list:
  if s >0.04:
    print(f"EPC0={s} > 0.04")


# ═══════════════════════════════════════════════════════════
# 第 3 题 — 函数（03 课）
# ═══════════════════════════════════════════════════════════
# 写函数 removal_rate(C0, Ce)，返回去除率（百分比，保留 2 位小数）
# 然后测试: removal_rate(75, 33.76) 应输出 54.99

print("\n第 3 题:")


# ↓↓↓ 你的代码 ↓↓↓
def removal_rate(C0,Ce):
    return f"{(C0 - Ce)/C0 * 100:.2f}%"
#or return round((C0 - Ce)/C0 * 100,2)
print(removal_rate(75,33.76))


# ═══════════════════════════════════════════════════════════
# 第 4 题 — 字典（04 课）
# ═══════════════════════════════════════════════════════════
# 把下面三个列表合并成一个字典列表，每个字典含 name/TP/DO 三个键
# 然后遍历打印 "站点 X: TP=Y mg/L, DO=Z mg/L"

print("\n第 4 题:")
sites = ["站点A", "站点B", "站点C"]
tp_vals = [0.12, 0.35, 0.08]
do_vals = [8.5, 7.1, 9.2]


# ↓↓↓ 你的代码 ↓↓↓
dir=[{'name':a,'TP':b,'DO':c} for a,b,c in zip(sites, tp_vals, do_vals)]
for d in dir:
    print(f"{d['name']}：TP={d['TP']} mg/L,DO={d['DO']} mg/L")


# ═══════════════════════════════════════════════════════════
# 第 5 题 — 文件读写（05 课）
# ═══════════════════════════════════════════════════════════
# 创建一个文本文件 review_test.txt，写入 3 行内容
# 然后用 with open 读回来，逐行打印（带行号）

print("\n第 5 题:")


# ↓↓↓ 你的代码 ↓↓↓
from pathlib import Path
out_file= Path.home()/'Desktop/python/review_test.txt'
with open(out_file, 'w',encoding='utf-8') as f:
    f.write("第一行\n第二行\n第三行\n")
with (open(out_file, 'r', encoding='utf-8') as f):
    lines=f.readlines()
    for i,line in enumerate(lines):
        line=line.strip()
        print(f"第{i+1}行：{line}")


# ═══════════════════════════════════════════════════════════
# 第 6 题 — 错误处理（06 课）
# ═══════════════════════════════════════════════════════════
# 写 safe_divide(a, b)，a÷b。b=0 时返回 "除数不能为零"，TypeError 返回 "类型错误"
# 测试: safe_divide(10, 2), safe_divide(10, 0), safe_divide("a", 2)

print("\n第 6 题:")


# ↓↓↓ 你的代码 ↓↓↓
def safe_divide(a, b):
  if b == 0:
    return "除数不能为零"
  try:
    return f"{(a / b):.2f}"
  except TypeError:
    return "类型错误"
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("a", 2))
       

# ═══════════════════════════════════════════════════════════
# 第 7 题 — 字符串（07 课）
# ═══════════════════════════════════════════════════════════
# 给定文件名 "WA3_profile_TP_1020.5.csv"，用 split 提取:
#   样品=WA3, 类型=profile, 指标=TP, 值=1020.5

print("\n第 7 题:")
fname = "WA3_profile_TP_1020.5.csv"


# ↓↓↓ 你的代码 ↓↓↓
if fname.endswith(".csv"):
    fname = fname[:-4] # 去掉 .csv 后缀
parts=fname.split("_")
print(f"样品={parts[0]},类型={parts[1]},指标={parts[2]},值={float(parts[3]):.1f}")



# ═══════════════════════════════════════════════════════════
# 第 8 题 — pathlib（08 课）
# ═══════════════════════════════════════════════════════════
# 用 pathlib 列出桌面 python 文件夹里所有 .py 文件的数量

print("\n第 8 题:")


# ↓↓↓ 你的代码 ↓↓↓
from pathlib import Path
p=Path.home() / "Desktop"/ "python"
py_files=list(p.rglob('*.py'))
print(len(py_files))

# ═══════════════════════════════════════════════════════════
# 第 9 题 — 推导式（09 课）
# ═══════════════════════════════════════════════════════════
# 用字典推导式创建一个字典: {1:1, 2:4, 3:9, 4:16, 5:25}
# （键是数字 1-5，值是其平方）

print("\n第 9 题:")


# ↓↓↓ 你的代码 ↓↓↓
d={x:x**2 for x in range(1,6)}
print(d)



# ═══════════════════════════════════════════════════════════
# 第 10 题 — 排序（10 课）
# ═══════════════════════════════════════════════════════════
# 对下面的字典列表按 PSI 降序排列，并给每个字典加 "rank" 键（1-6）

print("\n第 10 题:")
psi_samples = [
    {"name": "A", "PSI": 450},
    {"name": "B", "PSI": 520},
    {"name": "C", "PSI": 380},
    {"name": "D", "PSI": 610},
    {"name": "E", "PSI": 490},
    {"name": "F", "PSI": 550},
]


# ↓↓↓ 你的代码 ↓↓↓
ranked=sorted(psi_samples,key=lambda x:x['PSI'],reverse=True)
for rank,s in enumerate(ranked,start=1):
    s['rank']=rank
for s in ranked:
    print(f"样品 {s['name']}: PSI={s['PSI']} mg/kg, rank={s['rank']}")



# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("全部完成！独立做完 10 题 = 基础阶段毕业")
print("=" * 50)
