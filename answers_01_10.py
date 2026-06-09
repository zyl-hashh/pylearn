"""
第 1-10 课练习题参考答案

建议：先自己写完，翻车了再看答案。
看懂了改一改，看看改完还能不能跑。
"""

# ═══════════════════════════════════════════════════════════
# 01_basics 答案
# ═══════════════════════════════════════════════════════════

# 练习区是自由修改题，无标准答案。
# 确认你改了 my_number 和 my_name，改了 .2f 为 .4f，跑一遍看到变化即可。


# ═══════════════════════════════════════════════════════════
# 02_lists_loops 答案
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("02 答案")
print("=" * 50)

epc0 = [0.032, 0.045, 0.028, 0.051, 0.039, 0.047, 0.034, 0.041]
srp = [0.045, 0.052, 0.038, 0.061, 0.044, 0.055, 0.041, 0.049]
samples = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]
qmax = [0.623, 0.587, 0.541, 0.512, 0.598, 0.503, 0.601, 0.635]

# 练习 1 — 用 enumerate + 循环打印
print("练习 1:")
for i, val in enumerate(epc0, start=1):
    print(f"  样品 {i}: EPC0 = {val} mg/L")

# 练习 2 — 列表推导式 + zip
print("\n练习 2:")
diff = [s - e for s, e in zip(srp, epc0)]
print(f"  diff = {diff}")

# 练习 3 — 找 Qmax > 0.6
print("\n练习 3:")
for name, q in zip(samples, qmax):
    if q > 0.6:
        print(f"  {name}: Qmax = {q}")

# 练习 3 变体（用推导式）:
# high_q = [(n, q) for n, q in zip(samples, qmax) if q > 0.6]
# print(high_q)


# ═══════════════════════════════════════════════════════════
# 03_conditions_functions 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("03 答案")
print("=" * 50)

samples = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]
ce = [33.76, 34.85, 36.84, 37.73, 34.95, 38.03, 35.85, 34.46]
qmax = [0.623, 0.587, 0.541, 0.512, 0.598, 0.503, 0.601, 0.635]

import math

# 练习 1 — 写 calc_psi 函数
print("练习 1:")
def calc_psi(Q_mg_per_g, Ce):
    """计算 PSI = Q(mg/kg) / log10(Ce)"""
    Q_mg_per_kg = Q_mg_per_g * 1000
    return Q_mg_per_kg / math.log10(Ce)

wa3_psi = calc_psi(0.541, 36.84)
print(f"  WA3 PSI = {wa3_psi:.1f} mg/kg")

# 练习 2 — 分级函数 + 批量评判
print("\n练习 2:")
def classify_qmax(q):
    if q > 0.60:
        return "高"
    elif q > 0.55:
        return "中"
    else:
        return "低"

for name, q in zip(samples, qmax):
    print(f"  {name}: Qmax={q:.3f} → {classify_qmax(q)}")

# 练习 3 — 统计高/中/低数量
print("\n练习 3:")
high, mid, low = 0, 0, 0
for q in qmax:
    level = classify_qmax(q)
    if level == "高":
        high += 1
    elif level == "中":
        mid += 1
    else:
        low += 1
print(f"  高: {high}, 中: {mid}, 低: {low}")


# ═══════════════════════════════════════════════════════════
# 04_dict 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("04 答案")
print("=" * 50)

# 练习 1 — 三个列表 → 字典列表
print("练习 1:")
names = ["S1", "S2", "S3"]
temps = [24.5, 26.1, 22.8]
phs = [7.2, 7.8, 6.9]

stations = [
    {"name": n, "temp": t, "pH": p}
    for n, t, p in zip(names, temps, phs)
]
for s in stations:
    print(f"  站点 {s['name']}: 温度={s['temp']}°C, pH={s['pH']}")

# 练习 2 — 筛选 EPC0 > 0.04
print("\n练习 2:")
all_samples = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623, "EPC0": 0.032},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587, "EPC0": 0.045},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541, "EPC0": 0.028},
    {"name": "WA4", "PSI": 475.1, "Qmax": 0.512, "EPC0": 0.051},
    {"name": "WA5", "PSI": 521.1, "Qmax": 0.598, "EPC0": 0.039},
    {"name": "WA6", "PSI": 467.5, "Qmax": 0.503, "EPC0": 0.047},
    {"name": "WA7", "PSI": 524.0, "Qmax": 0.601, "EPC0": 0.034},
    {"name": "WA8", "PSI": 539.6, "Qmax": 0.635, "EPC0": 0.041},
]
for s in all_samples:
    if s["EPC0"] > 0.04:
        print(f"  {s['name']}: EPC0={s['EPC0']}")

# 练习 3 — 统计字典
print("\n练习 3:")
counts = {">500": 0, "<=500": 0}
for s in all_samples:
    if s["PSI"] > 500:
        counts[">500"] += 1
    else:
        counts["<=500"] += 1
print(f"  {counts}")


# ═══════════════════════════════════════════════════════════
# 05_file_io 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("05 答案")
print("=" * 50)

psidata = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623, "EPC0": 0.032},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587, "EPC0": 0.045},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541, "EPC0": 0.028},
    {"name": "WA5", "PSI": 521.1, "Qmax": 0.598, "EPC0": 0.039},
]

# 练习 1 — 写 CSV
print("练习 1:")
output_csv = "../Desktop/python/results_2026-05-21.csv"
with open(output_csv, "w", encoding="utf-8-sig") as f:
    f.write("name,PSI,Qmax\n")
    for s in psidata:
        f.write(f"{s['name']},{s['PSI']},{s['Qmax']}\n")
print(f"  已生成: {output_csv}")

# 练习 2 — 追加写日志
print("\n练习 2:")
log_file = "../Desktop/python/log.txt"
for i in range(1, 4):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"第{i}次实验记录\n")
print(f"  已追加到: {log_file}")

# 练习 3 — 读回并打印
print("\n练习 3:")
with open(output_csv, "r", encoding="utf-8-sig") as f:
    for line in f.readlines():
        print(f"  {line.strip()}")


# ═══════════════════════════════════════════════════════════
# 06_try_except 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("06 答案")
print("=" * 50)

# 练习 1 — safe_int
print("练习 1:")
def safe_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None

for test in ["42", "abc", "3.14", "100"]:
    print(f"  safe_int('{test}') = {safe_int(test)}")

# 练习 2 — check_files
print("\n练习 2:")
import os

def check_files(file_list):
    for fname in file_list:
        if os.path.exists(fname):
            print(f"  ✅ {fname}: 存在")
        else:
            print(f"  ⚠️ {fname}: 缺失")

check_files(["CLAUDE.md", "imaginary.txt", "python/01_basics.py"])

# 练习 3 — calc_psi_safe（Ce <= 1 返回 -1）
print("\n练习 3:")
def calc_psi_safe(Q_mg_g, Ce):
    try:
        if Q_mg_g <= 0:
            return -1
        if Ce <= 1:
            return -1
        Q_mg_kg = Q_mg_g * 1000
        return Q_mg_kg / math.log10(Ce)
    except (ValueError, ZeroDivisionError):
        return -1

print(f"  calc_psi_safe(0.823, 34.11) = {calc_psi_safe(0.823, 34.11):.1f}")
print(f"  calc_psi_safe(0.823, 0.5)   = {calc_psi_safe(0.823, 0.5)}")   # Ce 太小
print(f"  calc_psi_safe(-1, 34.11)    = {calc_psi_safe(-1, 34.11)}")    # Q 为负


# ═══════════════════════════════════════════════════════════
# 07_strings 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("07 答案")
print("=" * 50)

# 练习 1 — 提取 .tif 文件名
print("练习 1:")
filenames = ["WA1_PSI.tif", "WA2_EPC0.tif", "readme.txt", "data.xlsx"]
for f in filenames:
    if f.endswith(".tif"):
        name = f.replace(".tif", "")   # 或者 f.split(".")[0]
        print(f"  {name}")

# 练习 2 — 解析实验记录
print("\n练习 2:")
record = "WA3|34.85|0.8029|517.6"
parts = record.split("|")
print(f"  样品={parts[0]}, Ce={parts[1]}, Q={parts[2]}, PSI={parts[3]}")

# 练习 3 — f-string 表格
print("\n练习 3:")
print(f"{'样品名':<8} {'Ce':>8} {'Q':>8} {'PSI':>8}")
print("-" * 32)
data_rows = [
    ("WA1", 33.76, 0.8248, 533.5),
    ("WA2", 34.85, 0.8029, 517.6),
    ("WA3", 36.84, 0.7632, 488.9),
]
for row in data_rows:
    print(f"{row[0]:<8} {row[1]:>8.2f} {row[2]:>8.4f} {row[3]:>8.1f}")


# ═══════════════════════════════════════════════════════════
# 08_pathlib 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("08 答案")
print("=" * 50)

from pathlib import Path

# 练习 1 — 列出桌面 docx
print("练习 1:")
desktop = Path.home() / "Desktop"
for doc in desktop.glob("*.docx"):
    print(f"  {doc.name}")

# 练习 2 — 写文件再用 pathlib 读
print("\n练习 2:")
out_path = desktop / "python" / "lesson08_test.txt"
out_path.write_text("第一行内容\n第二行内容\n第三行内容", encoding="utf-8")
content = out_path.read_text(encoding="utf-8")
print(f"  写入并读取: {out_path.name}")
for i, line in enumerate(content.splitlines(), 1):
    print(f"    第{i}行: {line}")

# 练习 3 — find_files 函数
print("\n练习 3:")
def find_files(directory, suffix):
    dir_path = Path(directory)
    if not dir_path.exists():
        return []
    return list(dir_path.rglob(f"*{suffix}"))

py_files = find_files(Path.home() / "Desktop" / "vscode" / "python", ".py")
for f in py_files:
    print(f"  {f.name}")


# ═══════════════════════════════════════════════════════════
# 09_comprehensions 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("09 答案")
print("=" * 50)

# 练习 1 — 1-20 中偶数的平方
print("练习 1:")
even_squares = [n ** 2 for n in range(1, 21) if n % 2 == 0]
print(f"  {even_squares}")

# 练习 2 — 字典推导式 {name: PSI} 仅 PSI > 500
print("\n练习 2:")
psi_vals = [533.5, 517.6, 488.9, 475.1, 521.1, 467.5, 524.0, 539.6]
sample_names = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]
high_psi_dict = {n: p for n, p in zip(sample_names, psi_vals) if p > 500}
print(f"  {high_psi_dict}")

# 练习 3 — 嵌套推导式展平
print("\n练习 3:")
data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [x * 10 for row in data for x in row]
print(f"  {flattened}")


# ═══════════════════════════════════════════════════════════
# 10_sort_filter 答案
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("10 答案")
print("=" * 50)

measurements = [
    {"sample": "S1", "pH": 7.2, "DO": 8.5, "TP": 0.12},
    {"sample": "S2", "pH": 6.8, "DO": 7.1, "TP": 0.35},
    {"sample": "S3", "pH": 7.5, "DO": 9.2, "TP": 0.08},
    {"sample": "S4", "pH": 7.1, "DO": 6.3, "TP": 0.42},
    {"sample": "S5", "pH": 8.2, "DO": 8.9, "TP": 0.05},
]

# 练习 1 — 按 TP 排序
print("练习 1:")
by_tp = sorted(measurements, key=lambda m: m["TP"])
for m in by_tp:
    print(f"  样品 {m['sample']}: TP={m['TP']}")

# 练习 2 — 筛选 DO > 8.0 且 pH < 8.0
print("\n练习 2:")
good = [m for m in measurements if m["DO"] > 8.0 and m["pH"] < 8.0]
for m in good:
    print(f"  {m['sample']}: DO={m['DO']}, pH={m['pH']}")

# 练习 3 — 给 TP 加排名
print("\n练习 3:")
ranked_by_tp = sorted(measurements, key=lambda m: m["TP"])
for rank, m in enumerate(ranked_by_tp, start=1):
    m["TP_rank"] = rank
    print(f"  TP 第{rank}名: {m['sample']} (TP={m['TP']})")

print("\n" + "=" * 50)
print("全部答案打印完毕。")
print("=" * 50)
