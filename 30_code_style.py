"""
Python 第 30 课 —— 代码规范：写得像专业程序员

═══════════════════════════════════════════════════════════
为什么代码规范重要？
═══════════════════════════════════════════════════════════

面试官看你的代码，10 秒内决定第一印象：
  命名混乱、缩进不对、一行 200 个字符 → "这人没写过正经项目"
  整洁、有空格、命名一看就懂 → "这人至少有团队协作经验"

代码是写给人看的，顺便给机器执行。

═══════════════════════════════════════════════════════════
PEP 8 — Python 的"官方穿搭指南"
═══════════════════════════════════════════════════════════

PEP = Python Enhancement Proposal（Python 增强提案）
PEP 8 = Python 编码风格指南，全球 Python 程序员的公共约定。

记不住全部没关系——有自动检查工具帮你。
"""

# ═══════════════════════════════════════════════════════════
# 1. 命名规范 — 最重要的一条
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("命名规范速查")
print("=" * 50)
print("""
 类型          规则                    正确示例         错误示例
 ───────       ──────────             ────────         ────────
 变量/函数     snake_case（小写+下划线） calc_psi()       CalcPSI()
 常量          UPPER_CASE（全大写）     MAX_TEMP         maxTemp
 类名          PascalCase（大写开头）   WaterQuality     water_quality
 私有变量      下划线开头               _internal_var    internalVar
 模块/文件名   小写+下划线              plot_epc0.py     PlotEPC0.py

看懂了吗？你之前写的 calc_psi()、samples_raw、C0，
其实已经在遵循 PEP 8 了——你的直觉就是对的。
""")


# ═══════════════════════════════════════════════════════════
# 2. 缩进与空格 — 绝对不能含糊
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 缩进与空格规则                                            │
└─────────────────────────────────────────────────────────┘

  ✅ 用 4 个空格缩进（不要用 Tab，更不要混用）
     VS Code: 右下角点 "Spaces: 4"，勾选 "Insert Spaces"

  ✅ 每行不超过 79 个字符（注释/文档串不超过 72）
     太长用括号或反斜杠换行

  ✅ 逗号、冒号、分号后面加一个空格
     df[['TP', 'Silt', 'Clay']]       ← 逗号后面有空格
     x = (C0 - Ce) * V / m            ← 运算符两侧有空格

  ✅ 函数之间空两行，类之间空两行，函数内部逻辑块之间空一行

  ❌ 不要在行尾留空白（Trailing whitespace）
     VS Code: 设置搜 "trim trailing whitespace" 勾上
""")


# ═══════════════════════════════════════════════════════════
# 3. import 顺序
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ import 规范                                               │
└─────────────────────────────────────────────────────────┘

import 分三组，组间空一行：

  # 第 1 组：标准库（Python 自带的）
  import os
  import math
  from pathlib import Path

  # 第 2 组：第三方库（pip install 装的）
  import pandas as pd
  import matplotlib.pyplot as plt
  import numpy as np

  # 第 3 组：你自己写的模块
  from utils import calc_psi
  from config import BASE_DIR

禁止这样写：
  from pandas import *        # ❌ 污染命名空间，不知道导入了什么
  import os, sys, math        # ❌ 不要一行导入多个模块
""")


# ═══════════════════════════════════════════════════════════
# 4. 注释规范
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 注释 — 解释"为什么"而不是"做了什么"                         │
└─────────────────────────────────────────────────────────┘

  ❌ 废话注释：
     x = x + 1    # 把 x 加 1

  ✅ 有用的注释：
     x = x + 1    # 跳过表头行

  ❌ 注释掉的代码（删掉！Git 有历史记录，不需要保留）
     # old_result = calc_psi_old_method(data)

  ✅ Docstring — 函数的"说明书"
     def calc_psi(Q_mg_g, Ce):
         \"\"\"计算磷指数 PSI。

         Args:
             Q_mg_g: 单位吸附量 (mg/g)
             Ce: 平衡浓度 (mg/L)

         Returns:
             PSI 值 (mg/kg)。Ce <= 1 时返回 -1。
         \"\"\"
         ...
""")


# ═══════════════════════════════════════════════════════════
# 5. 实战：对比两段代码
# ═══════════════════════════════════════════════════════════

def bad_code():
    """这段代码能跑，但风格很差——你能找出几个问题？"""
    import math,os,sys
    def calc(Q,Ce):
        if Ce<=0:raise ValueError('bad')
        return Q*1000/math.log10(Ce)
    data=[{"name":"WA1","Ce":33.76,"q":0.823},{"name":"WA2","Ce":34.85,"q":0.803}]
    results=[]
    for d in data:
        r=calc(d["q"],d["Ce"])
        results.append(r)
    print(results)
    return results

def good_code():
    """同一段逻辑，符合 PEP 8 的版本"""
    import math

    def calc_psi(Q_mg_g, Ce):
        """计算磷指数 PSI。

        Args:
            Q_mg_g: 单位吸附量 (mg/g)
            Ce: 平衡浓度 (mg/L)

        Returns:
            PSI 值 (mg/kg)
        """
        if Ce <= 1:
            raise ValueError(f"Ce 必须 > 1，实际值为 {Ce}")
        return Q_mg_g * 1000 / math.log10(Ce)

    samples = [
        {"name": "WA1", "Ce": 33.76, "Q": 0.823},
        {"name": "WA2", "Ce": 34.85, "Q": 0.803},
    ]

    psi_results = [calc_psi(s["Q"], s["Ce"]) for s in samples]
    print(psi_results)
    return psi_results


print("=" * 50)
print("bad_code 的问题（你能找出多少个？）：")
print("=" * 50)
problems = [
    "1. 一行 import 了 math, os, sys 三个模块",
    "2. 函数名 calc 含义不清（calc 什么？）",
    "3. if 和 raise 写在同一行，难读",
    "4. 异常消息 'bad' 无意义",
    "5. 字典键 'q' 和参数 Q 不一致",
    "6. results = [] + for + append 可用推导式一行搞定",
    "7. 缺少函数文档串 (docstring)",
    "8. 变量 r 名字太短，不知道是什么",
]
for p in problems:
    print(f"  {p}")


# ═══════════════════════════════════════════════════════════
# 6. 自动检查工具（让机器帮你挑刺）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("自动检查工具")
print("=" * 50)
print("""
你不用手动逐行检查——有工具帮你：

  flake8    → 检查是否符合 PEP 8
  pip install flake8
  flake8 my_script.py         # 列出所有不规范的地方

  black     → 自动格式化代码（一键修复）
  pip install black
  black my_script.py           # 自动把代码格式化成标准风格

  isort     → 自动排序 import
  pip install isort
  isort my_script.py

  pylint    → 全面检查（风格+逻辑+复杂度）
  pip install pylint
  pylint my_script.py

建议：先用 black 格式化，再用 flake8 检查剩余问题。
面试时提一句"我用 black 做自动格式化"，面试官会点头。
""")


# ═══════════════════════════════════════════════════════════
# 练习
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("练习")
print("=" * 50 + "\n")

print("""
1. 把你的 project_psi_full.py 用 black 格式化：
   pip install black
   black python/project_psi_full.py

2. 看一下 black 改了哪些地方（git diff 如果有的话）

3. 把下面这段烂代码改成符合 PEP 8 的版本：
""")

dirty = '''
import math,os,sys
def f(x):
    if x>0:return math.log10(x)
    else:return -1
data=[33.76,34.85,36.84]
r=[]
for d in data:
    v=f(d)
    r.append(v)
print(r)
'''

print(dirty)

print("""
4. 对比你的版本和我上面的 good_code 函数，看看有哪些差异。
""")


# ═══════════════════════════════════════════════════════════
# 复习练习（10 课：sorted + lambda）
# 难度：⭐⭐（两个知识点组合）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：对代码文件按行数排序")
print("=" * 50)

print("""
═══════════════ 分步引导 ═══════════════

第 1 步：用 pathlib 扫描 python/ 文件夹，拿到每个 .py 文件
  from pathlib import Path
  py_dir = Path.home() / "Desktop" / "vscode" / "python"
  files = list(py_dir.glob("*.py"))

第 2 步：统计每个文件的行数，做成 (文件名, 行数) 元组列表
  result = []
  for f in files:
      lines = len(f.read_text(encoding="utf-8").splitlines())
      result.append((f.name, lines))

第 3 步：用 sorted() 按行数降序，打印
  sorted(result, key=lambda x: x[1], reverse=True)

══════════════════════════════
""")
print("=" * 50 + "\n")

# ↓↓↓ 你的代码 ↓↓↓



# ═══════════════════════════════════════════════════════════
# 就业前瞻：Code Review — 你的代码要被人看
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】Code Review — 程序员的日常")
print("=" * 50)
print("""
你写的每一行代码，在公司里都会被同事 Review（审查）。

Code Review 里最常见的评论：
  "变量名改一下，'data' 太泛了"
  "这个函数太长，拆成两个"
  "import 顺序不对，跑一下 isort"
  "这里加个注释解释为什么用 1.5 而不是 2.0"

如果你的代码整洁、命名规范、有 docstring，
Review 一轮过。如果风格混乱，Review 来回 5 轮，
同事对你的印象就是"这人不会写代码"。

你学了 PEP 8 + black + flake8，已经比大部分
"我 Python 写得好但规范完全不管"的求职者强了。
这不是锦上添花——这是基本素质。
""")
