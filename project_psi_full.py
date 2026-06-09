"""
============================================================
综合项目：吸附实验 PSI 批量计算与报告生成
============================================================

用 1-10 课全部知识，从原始数据到输出报告一气呵成。

═══════════════════════════════════════════════════════════
复习清单 — 本项目用到的所有知识点
═══════════════════════════════════════════════════════════

【01 变量与类型】
  变量赋值, f-string, int, float, str, type()

【02 列表与循环】
  列表创建, for 循环, enumerate(序号+值), zip(两个列表配对),
  range(), 列表推导式

【03 条件与函数】
  def 函数, return 返回值,
  if / elif / else, 比较运算符 (>, <, ==, >=, <=),
  and / or 组合条件

【04 字典】
  字典创建 {键: 值}, 字典取值 dict["键"],
  .items() .keys() .values(), 字典列表 [{...}, {...}],
  统计字典计数

【05 文件读写】
  with open("文件名", "w") as f, f.write(),
  encoding="utf-8-sig" (Excel不乱码),
  "w" 写模式 / "a" 追加模式

【06 错误处理】
  try / except, raise ValueError

【07 字符串】
  split() 切分, join() 拼接, startswith() / endswith(),
  f"{变量:.2f}" 小数控制, f"{变量:>8}" 对齐

【08 路径】
  from pathlib import Path, Path("路径"),
  用 / 拼接路径, .exists(), .mkdir(exist_ok=True),
  .read_text(), .write_text()

【09 推导式】
  列表推导式 [表达式 for x in 列表 if 条件],
  字典推导式 {键: 值 for ...}

【10 排序与过滤】
  sorted(列表, key=lambda x: x["字段"]),
  sorted(..., reverse=True) 降序,
  filter(lambda x: 条件, 列表),
  enumerate(列表, start=1) 生成排名

═══════════════════════════════════════════════════════════
项目任务
═══════════════════════════════════════════════════════════

你有 8 个沉积物样品 (WA1-WA8)，进行了磷吸附实验。
实验条件：初始浓度 C0=75 mg/L，溶液体积 V=0.020 L，吸附剂质量 m=1 g

任务流程：
  1. 用字典列表存储 8 个样品的 Ce 数据
  2. 写 calc_Q() 函数计算吸附量
  3. 写 calc_PSI() 函数计算磷指数
  4. 用循环 + 推导式批量计算全部样品
  5. 用 sorted() 按 PSI 降序排名
  6. 统计 PSI 等级分布（高>520, 中>480, 低<=480）
  7. 用 f-string 打印对齐的报告表格
  8. 用 pathlib 创建输出目录，把结果写 CSV

═══════════════════════════════════════════════════════════
核心公式
═══════════════════════════════════════════════════════════

  Q (mg/g) = (C0 - Ce) × V / m    — 吸附量
  PSI (mg/kg) = Q(mg/g) × 1000 / log₁₀(Ce)    — 磷指数

═══════════════════════════════════════════════════════════
请在下面的 "你的代码区" 中完成。
═══════════════════════════════════════════════════════════
"""

import math
from pathlib import Path

# ╔══════════════════════════════════════════════════════════╗
# ║  第 1 步：准备数据                                       ║
# ║  用字典列表存储 8 个样品的 Ce 值                           ║
# ╚══════════════════════════════════════════════════════════╝

C0 = 75.0  # 初始浓度 mg/L
V = 0.020  # 溶液体积 L
m = 1.0  # 吸附剂质量 g

# TODO: 用字典列表定义 8 个样品，每个字典有 "name" 和 "Ce" 两个键
# 提示：参考 04_dict.py 第 3 节

samples_raw = [
    {"name": "WA1", "Ce": 33.76},
    {"name": "WA2", "Ce": 34.85},
    {"name": "WA3", "Ce": 36.84},
    {"name": "WA4", "Ce": 37.73},
    {"name": "WA5", "Ce": 34.95},
    {"name": "WA6", "Ce": 38.03},
    {"name": "WA7", "Ce": 35.85},
    {"name": "WA8", "Ce": 34.46},
]


# ╔══════════════════════════════════════════════════════════╗
# ║  第 2 步：写计算函数                                     ║
# ║  calc_Q(Ce)     → 返回吸附量 Q (mg/g)                    ║
# ║  calc_PSI(Q, Ce) → 返回磷指数 PSI (mg/kg)                ║
# ║  都要做输入验证：Ce > 0                                   ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: 定义 calc_Q 函数
# 公式：Q = (C0 - Ce) × V / m
# 如果 Ce >= C0 抛出异常（浓度不能大于初始浓度）


def calc_Q(Ce):
    if Ce <= 0:
        raise ValueError("数据异常")
    if Ce >= C0:
        raise ValueError("数据异常")
    Q = (C0 - Ce) * V / m
    return Q


# TODO: 定义 calc_PSI 函数
# 公式：PSI = Q(mg/g) × 1000 / log₁₀(Ce)
# 如果 Ce <= 1 抛出异常（log10(≤1) 无意义）


def calc_PSI(Q_mg_g, Ce):
    if Ce <= 0:
        raise ValueError("数据异常")
    if Ce <= 1:
        raise ValueError("数据异常")
    PSI = Q_mg_g * 1000 / math.log(Ce, 10)
    return PSI


# ╔══════════════════════════════════════════════════════════╗
# ║  第 3 步：批量计算                                        ║
# ║  用循环 + 字典操作，给每个样品添加 Q 和 PSI 字段            ║
# ║  然后用推导式创建新列表（只保留计算成功的样品）              ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: 遍历 samples_raw，计算每个样品的 Q 和 PSI，存回字典
# 提示：s["Q"] = calc_Q(s["Ce"])，同理设 s["PSI"]

samples = []  # 计算成功后放这里

# 你的循环代码 ↓


# ╔══════════════════════════════════════════════════════════╗
# ║  第 4 步：排序与排名                                      ║
# ║  用 sorted(key=lambda) 按 PSI 降序排列                    ║
# ║  用 enumerate(start=1) 给排名                             ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: 按 PSI 降序排列，然后加 rank 字段
# 提示：sorted(samples, key=lambda s: s["PSI"], reverse=True)

# 你的排序代码 ↓


# ╔══════════════════════════════════════════════════════════╗
# ║  第 5 步：统计等级分布                                     ║
# ║  高 > 520, 中 > 480, 低 ≤ 480                            ║
# ║  用字典计数器（参考 04_dict 第 4 节）                       ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: 创建 {"高":0, "中":0, "低":0}，遍历统计
# 提示：要用 samples 列表（不是 samples_raw）

# 你的统计代码 ↓


# ╔══════════════════════════════════════════════════════════╗
# ║  第 6 步：打印报告                                        ║
# ║  用 f-string 对齐，打印完整表格                            ║
# ║  表头：排名 | 样品 | Ce(mg/L) | Q(mg/g) | PSI(mg/kg) | 等级   ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: 打印表头，然后遍历 ranked_samples 逐行打印
# 提示：参考 07_strings 第 3 节表格对齐

print("\n" + "=" * 65)
print("  吸附实验 PSI 计算结果")
print("=" * 65)

# 你的表头打印代码 ↓


# 你的数据行打印代码 ↓


# 打印等级分布

# ╔══════════════════════════════════════════════════════════╗
# ║  第 7 步：输出 CSV                                        ║
# ║  用 pathlib 创建输出目录，写 CSV（UTF-8 BOM，Excel 可开）     ║
# ╚══════════════════════════════════════════════════════════╝

# TODO: Path.home() / "Desktop/python" 创建目录
# TODO: 写入 results_psi.csv，包含排名、样品、Ce、Q、PSI、等级

# 你的 CSV 输出代码 ↓


print("\n完成！")
import math
from pathlib import Path

C0 = 75.0  # 初始浓度 mg/L
V = 0.020  # 溶液体积 L
m = 1.0
samples_raw = [
    {"name": "WA1", "Ce": 33.76},
    {"name": "WA2", "Ce": 34.85},
    {"name": "WA3", "Ce": 36.84},
    {"name": "WA4", "Ce": 37.73},
    {"name": "WA5", "Ce": 34.95},
    {"name": "WA6", "Ce": 38.03},
    {"name": "WA7", "Ce": 35.85},
]


def cacl_Q(Ce):
    if Ce <= 0:
        raise ValueError("数据异常")
    if Ce >= C0:
        raise ValueError("数据异常")
    Q = (C0 - Ce) * V / m
    return Q


def calc_PSI(Q, Ce):
    if Ce <= 0:
        raise ValueError("数据异常")
    PSI = Q * 1000 / math.log(Ce, 10)
    return PSI


samples = []
for s in samples_raw:
    try:
        s["Q"] = cacl_Q(s["Ce"])
        s["PSI"] = calc_PSI(s["Q"], s["Ce"])
    except ValueError as e:
        print(e)
samples = [s for s in samples_raw if "PSI" in s]

ranked_samples = sorted(samples, key=lambda s: s["PSI"], reverse=True)
for i, s in enumerate(ranked_samples, start=1):
    s["rank"] = i

grade = {"高": 0, "中": 0, "低": 0}
for s in samples:
    if s["PSI"] > 520:
        grade["高"] += 1
    elif s["PSI"] < 480:
        grade["低"] += 1
    else:
        grade["中"] += 1


def grade_p(PSI):
    if PSI > 520:
        return "高"
    elif PSI < 480:
        return "低"
    else:
        return "中"


for s in ranked_samples:
    s["grade"] = grade_p(s["PSI"])
print(f"{'排名':<4}|{'样品':<4}|{'Ce(mg/L)':<6}{'PSI(mg/kg)':<8}{'等级':>6}")
for s in ranked_samples:
    print(f"{s['rank']:4}{s['name']:<4}{s['Ce']:<4}{s['PSI']:<8}{s['grade']:>6}")

out_dir = Path.home() / "Desktop/python"
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "result_psi.csv"
with open(out_file, "w", encoding="utf-8-sig") as f:
    f.write("排名,样品,Ce(mg/L),Q(mg/g),PSI(mg/kg),等级\n")
    for s in ranked_samples:
        f.write(f"{s['rank']},{s['name']},{s['Ce']},{s['Q']},{s['PSI']},{s['grade']}\n")
