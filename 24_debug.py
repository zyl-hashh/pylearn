"""
Python 第 24 课 —— 调试技巧

以前你 debug 靠 print() 和问我。这节课学真正的调试工具。
掌握 pdb 和常见 bug 类型，遇到报错自己能定位。
"""

# ═══════════════════════════════════════════════════════════
# 1. 用 breakpoint() 暂停程序
# ═══════════════════════════════════════════════════════════

def calc_psi(Q, Ce):
    """计算 PSI，中间插一个断点看看数据长什么样"""
    import math
    breakpoint() #会在这里暂停，让你检查 Q 和 Ce 的值
    # 暂停后输入:  p Q    → 打印 Q 的值
    #              p Ce   → 打印 Ce 的值
    #              c      → 继续运行
    #              q      → 退出
    if Ce <= 1:
        return -1
    return Q * 1000 / math.log10(Ce)

# 取消下面这行注释试试:
result = calc_psi(34.11, 0.833)
# 运行后程序暂停，你在终端里交互式检查变量
print(result)
print("这节课不自动运行，而是教你怎么主动调试。")

# ═══════════════════════════════════════════════════════════
# 2. 常见 Bug 类型 — 认出它们，就能自己解决
# ═══════════════════════════════════════════════════════════

print("══════════════════════════════════════")
print("常见报错速查表")
print("══════════════════════════════════════")

# (a) NameError — 变量没定义
try:
    print(undefined_var)
except NameError as e:
    print(f"NameError: {e}")
    print("  → 变量名打错了或还没赋值\n")

# (b) TypeError — 类型不对
try:
    result = "PSI = " + 533.5       # 字符串不能直接 + 数字
except TypeError as e:
    print(f"TypeError: {e}")
    print("  → 用 f-string: f'PSI = {533.5}'\n")

# (c) IndexError — 列表下标越界
data = [1, 2, 3]
try:
    print(data[5])
except IndexError as e:
    print(f"IndexError: {e}")
    print("  → 下标 5 超出范围（共 3 个元素）\n")

# (d) KeyError — 字典键不存在
s = {"name": "WA1", "TP": 996}
try:
    print(s["PSI"])
except KeyError as e:
    print(f"KeyError: {e}")
    print("  → 用 s.get('PSI', '默认值') 安全取值\n")

# (e) AttributeError — 对象没这个方法
try:
    x = 42
    x.append(10)                   # int 没有 append
except AttributeError as e:
    print(f"AttributeError: {e}")
    print("  → 42 是整数不是列表，没有 append 方法\n")

# (f) IndentationError — 缩进错误
# 下面这段取消注释会直接在编辑器中报错，无法运行:
#if True:
#print("缩进错了")


# ═══════════════════════════════════════════════════════════
# 3. 调试三步法
# ═══════════════════════════════════════════════════════════

print("══════════════════════════════════════")
print("调试三步法")
print("══════════════════════════════════════")
print("""
遇到报错不要慌，按这个来：

  1. 读最后一行
     → KeyError: 'TP'  ← 问题在这：找不到 'TP'
     → TypeError: can only concatenate str  ← 类型错了

  2. 看 Traceback 从下往上找自己写的文件
     忽略 pandas/numpy 内部的报错，找你自己的文件名:
     File "my_script.py", line 42, in <module>
                         ↑ 问题在这一行

  3. 在该行前面加 print() 或 breakpoint()
     print(df.columns)  → 看到底有哪些列
     breakpoint()       → 交互式检查

90% 的 bug 靠这三步自己解决，不用问人。
""")


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 故意制造一个 KeyError 和 IndexError，用 try/except 捕获并打印友好提示

print("练习 1:")
# ↓↓↓
try:
    s = {"name": "WA1", "TP": 996}
    print(s["PSI"])   # KeyError
except KeyError as e:
    print(f"KeyError: {e}")
    print("  → 用 s.get('PSI', '默认值') 安全取值\n")
try:
    data = [1, 2, 3]
    print(data[5])    # IndexError
except IndexError as e:
    print(f"IndexError: {e}")
    print("  → 下标 5 超出范围（共 3 个元素）\n")


print("\n")

# ── 练习 2 ──
# 下面代码有 bug（TypeError），请修复它
#  numbers = [1, 2, 3, "4", 5]
#  total = sum(numbers)

print("练习 2:")
# ↓↓↓
numbers = [1, 2, 3, "4", 5]
total = sum(int(n) for n in numbers)  # 把每个元素都转成整数再求和
print(f"总和: {total}")


# ═══════════════════════════════════════════════════════════
# 复习练习（16-17 课：groupby + merge）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：用 pandas 做分组统计 + 合并")
print("=" * 50 + "\n")

# 任务：用 pd.read_excel 读 sediment sheet，改短列名
# 然后按 ID 分组，计算 TP 的 mean 和 std

# ↓↓↓ 你的代码 ↓↓↓
import pandas as pd
from pathlib import Path
p=Path.home()/'desktop/赣江数据/WA.xlsx'
df=pd.read_excel(p,sheet_name='sediment')
col=list(df.columns)
col[4]='TP'
df.columns=col
f=df.groupby('ID')['TP'].agg(['mean','std'])
print(f)


# ═══════════════════════════════════════════════════════════
# 就业前瞻：程序员的终端
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】程序员的终端长什么样")
print("=" * 50)
print("""
程序员的工作界面通常只有三个东西：

  左边：代码编辑器（VS Code / PyCharm）
  右边：终端（跑程序、打命令）
  上边：浏览器（看文档、测试网页）

终端不是 Windows 的 CMD（那个太弱了），而是：

  Bash / Zsh    → Linux/Mac 默认 Shell
  PowerShell    → Windows 新一代 Shell
  Git Bash      → 你现在用的，在 Windows 模拟 Linux

终端进阶：
  - 按 ↑ 回到上一条命令（不用重新敲）
  - Tab 自动补全文件名
  - Ctrl+C 停止正在运行的程序
  - Ctrl+R 搜索历史命令

今天试试：
  在 Git Bash 里输入 history，回车
  → 看到你敲过的所有命令。这就是你"用终端"的历史。

你每次在这里 python xxx.py，就是在用程序员的终端。
""")
