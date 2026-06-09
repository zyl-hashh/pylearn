"""
Python 入门第 5 课 —— 文件读写

把计算结果存到 txt 文件、从 txt 读数据，不用每次都开 Excel。
这是自动化报告的第一步——你的数据算出结论后自动写成文件。
"""

# ═══════════════════════════════════════════════════════════
# 1. 写入文本文件 — open() + write()
# ═══════════════════════════════════════════════════════════

# 最基本的三步：
#   open("文件名", "w")  →  w = write 写模式（会覆盖！）
#   f.write("内容")
#   f.close()           →  一定要关，否则数据可能没写进去

f = open("output_lesson05.txt", "w", encoding="utf-8")
f.write("这是第一行\n")        # \n = 换行
f.write("这是第二行\n")
f.write(f"PI = {3.14159:.2f}\n")
f.close()
print("文件已写入: output_lesson05.txt")

# 推荐写法：用 with，自动关闭文件（不用 f.close()）
with open("output_lesson05.txt", "a", encoding="utf-8") as f:
    f.write("追加一行（a 模式不会覆盖，加在末尾）\n")
# 缩进结束，文件自动关闭


# ═══════════════════════════════════════════════════════════
# 2. 读取文本文件
# ═══════════════════════════════════════════════════════════

# 一次性读完：
with open("output_lesson05.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("文件内容:\n" + content)

# 逐行读：
with open("output_lesson05.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()           # 返回一个列表，每行一个元素
    for i, line in enumerate(lines):
        line = line.strip()          # 去掉末尾的 \n
        print(f"第{i+1}行: {line}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 写 CSV 文件 — 表格数据最常用的格式
# ═══════════════════════════════════════════════════════════

# CSV 就是逗号分隔，Excel 可以直接打开
with open("samples_lesson05.csv", "w", encoding="utf-8-sig") as f:
    # utf-8-sig = 带 BOM，Excel 打开不乱码
    f.write("样品,PSI,Qmax,EPC0\n")           # 表头
    f.write("WA1,533.5,0.623,0.032\n")
    f.write("WA2,517.6,0.587,0.045\n")
    f.write("WA3,488.9,0.541,0.028\n")

print("samples_lesson05.csv 已生成 — 双击用 Excel 打开试试")

# 当然，实际代码里你不会手写每一行，用循环：
samples = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541},
]

with open("samples_loop_lesson05.csv", "w", encoding="utf-8-sig") as f:
    f.write("样品,PSI,Qmax\n")
    for s in samples:
        f.write(f"{s['name']},{s['PSI']},{s['Qmax']}\n")
print("samples_loop_lesson05.csv 已生成")


# ═══════════════════════════════════════════════════════════
# 4. 读写模式速查
# ═══════════════════════════════════════════════════════════
#
#   "r"  = read  只读（默认），文件不存在会报错
#   "w"  = write 写（覆盖原有内容），文件不存在会创建
#   "a"  = append 追加到末尾，文件不存在会创建
#   "x"  = 新建文件，文件已存在会报错（防止误覆盖）
#   "rb"/"wb" = 二进制读写（图片、PDF 用）
#
#   科研最常用："w" 写新报告，"r" 读数据，"a" 续写日志


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# 数据：
psidata = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623, "EPC0": 0.032},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587, "EPC0": 0.045},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541, "EPC0": 0.028},
    {"name": "WA5", "PSI": 521.1, "Qmax": 0.598, "EPC0": 0.039},
]

# ── 练习 1 ──
# 用上面的数据生成 results.csv，包含 name, PSI, Qmax 三列
# 然后在文件名里加上今天的日期（手动填）

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
output_csv = "../Desktop/python/results_2026-05-21.csv"
with open("results0521.csv","w",encoding="utf-8") as f:
    f.write("name,PSI,Qmax\n")
    for s in psidata:
        f.write(f"{s['name']},{s['PSI']},{s['Qmax']}\n")


print("\n")

# ── 练习 2 ──
# 写一个日志文件 log.txt（用 "a" 追加模式）
# 写入 3 行 "第N次实验记录"

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
with open("log.txt","a",encoding="utf-8-sig") as f:
    for i in range(3):
        f.write(f"第{i+1}次实验记录\n")

print("\n")

# ── 练习 3 ──
# 读取你刚才生成的 results.csv，打印每一行的内容
# 提示: readlines() 然后 strip()

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
with open("results0521.csv","r",encoding="utf-8-sig") as f:
    lines = f.readlines()
    for line in lines:
        print(f"{line.strip()}")


print("\n完成！下一步：06_try_except.py")
