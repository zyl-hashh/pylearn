"""
Python 入门第 7 课 —— 字符串处理

你的实验数据文件命名、样品编号、报告里的化学符号，
全是在处理字符串。这节课教你"庖丁解牛"。
"""

# ═══════════════════════════════════════════════════════════
# 1. 基本操作 — 拼接、重复、大小写、查找
# ═══════════════════════════════════════════════════════════

name = "  Wangan Dam  "

# 去首尾空白
print(f"原始: |{name}|")
print(f"去空白: |{name.strip()}|")       # 去两边
print(f"去左边: |{name.lstrip()}|")      # 只去左边
print(f"去右边: |{name.rstrip()}|")      # 只去右边

# 大小写
txt = "Poyang Lake"
print(f"全大写: {txt.upper()}")
print(f"全小写: {txt.lower()}")
print(f"首字母大写: {txt.title()}")

# 查找与替换
full = "WA1_Sediment_0-5cm"
print(f"包含 Sediment 吗? {'Sediment' in full}")    # True
print(f"Sediment 位置: {full.find('Sediment')}")    # 4（第5个字符，从0数）
print(f"替换: {full.replace('Sediment', 'Water')}") # WA1_Water_0-5cm

# 字符串*数字 = 重复
print("─" * 40)

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 分割与拼接 — 科研里最常用的操作
# ═══════════════════════════════════════════════════════════

# split() 切分字符串 → 得到列表
filename = "WA3_0-5cm_TP_832.5.csv"
parts = filename.split("_")        # 按 _ 切开
print(f"文件名: {filename}")
print(f"切开: {parts}")
# ['WA3', '0-5cm', 'TP', '832.5.csv']
print(f"  样品: {parts[0]}")
print(f"  深度: {parts[1]}")
print(f"  指标: {parts[2]}")

# join() 把列表粘回字符串
print(f"粘回去: {' | '.join(parts)}")    # WA3 | 0-5cm | TP | 832.5.csv
print(f"用逗号粘: {', '.join(['WA1', 'WA2', 'WA3'])}")

# split() 的高级用法：只切 N 次
line = "WA1, 万安大坝, 2026-05-21, 表层"
print(f"只切一次: {line.split(', ', 1)}")   # ['WA1', '万安大坝, 2026-05-21, 表层']

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 格式化 — f-string 全家桶
# ═══════════════════════════════════════════════════════════

psi = 533.5
ratio = 0.8532

# 数字对齐
print(f"PSI 右对齐 10 格: |{psi:>10}|")     # > = 右对齐
print(f"PSI 左对齐 10 格: |{psi:<10}|")     # < = 左对齐
print(f"PSI 居中 10 格:   |{psi:^10}|")     # ^ = 居中

# 百分比
print(f"比率: {ratio:.1%}")                  # 85.3%
print(f"比率: {ratio:.2%}")                  # 85.32%
# 科学计数法
big = 1234567
small = 0.0000123
print(f"科学计数: {big:.2e}")               # 1.23e+06
print(f"科学计数: {small:.2e}")             # 1.23e-05

# 表格级对齐 — 报告生成必备
print("\n样品报告表格:")
print(f"{'样品':<8} {'PSI':>8} {'Qmax':>8} {'等级':<6}")
print("_" * 32)
for record in [("WA1", 533.5, 0.623, "高"),
               ("WA2", 517.6, 0.587, "中"),
               ("WA8", 539.6, 0.635, "高")]:
    print(f"{record[0]:<8} {record[1]:>8.1f} {record[2]:>8.3f} {record[3]:<6}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 子串判断与正则预览
# ═══════════════════════════════════════════════════════════

# startswith / endswith — 判断文件名模式
files = ["WA1_EPC0.tif", "WA1_PSI.tif", "README.md", "data.xlsx"]

for f in files:
    if f.endswith(".tif"):
        print(f"图片: {f}")
    elif f.endswith(".md"):
        print(f"文档: {f}")
    elif f.endswith(".xlsx") or f.endswith(".csv"):
        print(f"数据: {f}")
    else:
        print(f"其他: {f}")

# 判断样品编号格式
sample_id = "WA12"
if sample_id.startswith("WA") and sample_id[2:].isdigit():
    # [2:] = 从第 2 个字符开始到末尾，isdigit() = 全是数字？
    print(f"  {sample_id} 是有效编号")
else:
    print(f"  {sample_id} 格式不对")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 给定文件名列表，提取所有 .tif 文件的名字（不含扩展名）
# 提示: .replace(".tif", "") 或 .split(".")[0]
filenames = ["WA1_PSI.tif", "WA2_EPC0.tif", "readme.txt", "data.xlsx"]

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
for f in filenames:
    if f.endswith(".tif"):
        f=f.split('.')[0]
        print(f"{f}")


print("\n")

# ── 练习 2 ──
# 给定实验记录字符串，解析出样品名和三个数值
# 输入: "WA3|34.85|0.8029|517.6"
# 输出: 样品=WA3, Ce=34.85, Q=0.8029, PSI=517.6
record = "WA3|34.85|0.8029|517.6"

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
re=record.split('|')
print(f"样品={re[0]}，Ce={re[1]},Q={re[2]},PSI={re[3]}")


print("\n")

# ── 练习 3 ──
# 用 f-string 对齐，生成一个 4 列对齐的表格头，并打印 3 行数据
# 列名: 样品名(左对齐8格) | Ce(右对齐8格) | Q(右对齐8格) | PSI(右对齐8格)
# 数据自拟

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
ex=["样品名","Ce","Q","PSI"]
l1=["1","3","3","5"]
l2=["2","3","3","5"]
l3=["3","3","3","5"]
fl1=[ex,l1,l2,l3]
for n in fl1:
    print(f"{n[0]:<8}{n[1]:<8}{n[2]:>8}{n[3]:>8}")


print("\n完成！下一步：08_pathlib.py")
