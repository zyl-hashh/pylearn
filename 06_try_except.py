"""
Python 入门第 6 课 —— 错误处理 try/except

错误处理不是"防止出 bug"，而是"出 bug 时优雅地处理"。
你的科研代码读几十个 Excel，中间有一个文件缺失、格式不对
就整个崩掉——用 try/except 可以跳过坏的，继续处理后面的。
"""

# ═══════════════════════════════════════════════════════════
# 1. 没有 try/except 会怎样？— 直接崩
# ═══════════════════════════════════════════════════════════

# 下面这行如果取消注释运行，整个脚本就停了，后面全不跑
# print(1 / 0)    # ZeroDivisionError
# print("这行永远不会执行")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 基本格式 — try/except 兜底
# ═══════════════════════════════════════════════════════════

# 尝试做一件事，失败了走备用方案
try:
    result = 10 / 2
    print(f"10/2 = {result}")
except ZeroDivisionError:
    print("除数不能为 0！")

try:
    result = 10 / 0
    print(f"10/0 = {result}")               # 这行不会执行
except ZeroDivisionError:
    print("跳过：除数不能为 0！")

print("程序继续运行，没崩溃\n")

# 多个 except，每种错误分别处理：
x = "abc"
try:
    num = int(x)            # 字符串转不了整数
    print(10 / num)
except ValueError:
    print(f"'{x}' 不是数字，无法转换")
except ZeroDivisionError:
    print("除数为 0")
except Exception as e:      # catch-all，抓到所有没想到的错误
    print(f"未知错误: {e}")

# else：没报错才走（可选）
# finally：不管报不报错都走（可选，比如关文件）
try:
    print("尝试中...")
except Exception:
    print("出错了")
else:
    print("一切顺利")
finally:
    print("无论怎样我都执行")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 科研场景 — 批量读 Excel，缺失文件不崩
# ═══════════════════════════════════════════════════════════

files_to_read = [
    "WA.xlsx",              # 这个应该存在
    "不存在的数据.csv",       # 这个不存在
    "格式错误的数据.csv",     # 这个也不存在
    "WA.xlsx",              # 再读一次好的
]

import os

for fname in files_to_read:
    try:
        size = os.path.getsize(fname)  # 获取文件大小
        print(f"  ✅ {fname}: {size} 字节")
    except FileNotFoundError:
        print(f"  ⚠️ {fname}: 文件不存在，跳过")
    except Exception as e:
        print(f"  ❌ {fname}: {e}")

# 没有 try/except 的话，第一个缺失文件就让整个脚本崩溃了！

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. raise — 主动抛出异常
# ═══════════════════════════════════════════════════════════

# 有时候数据不合要求，你想主动叫停
def calc_psi(Q_mg_g, Ce):
    """计算 PSI，输入不合法时主动报错"""
    import math

    if Q_mg_g <= 0:
        raise ValueError(f"Q 必须大于 0，实际值为 {Q_mg_g}")
    if Ce <= 0:
        raise ValueError(f"Ce 必须大于 0，实际值为 {Ce}")

    Q_mg_kg = Q_mg_g * 1000
    return Q_mg_kg / math.log10(Ce)

# 正常调用：
try:
    print(f"PSI = {calc_psi(0.823, 34.11):.1f} mg/kg")
except ValueError as e:
    print(e)

# 非法输入：
try:
    print(calc_psi(-1, 34.11))
except ValueError as e:
    print(f"计算失败: {e}")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 写一个安全的整数输入函数 safe_int(s)
# 如果 s 能转成整数就返回整数，否则返回 None
# 测试: "42", "abc", "3.14", "100"

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
for test in ["42", "abc", "3.14", "100"]:
    print(f"safe_int('{test}') = {safe_int(test)}")
 # 100


print("\n")

# ── 练习 2 ──
# 写一个批量文件检查函数 check_files(file_list)
# 遍历列表中的每个文件名，打印"存在"或"缺失"
# 文件不存在时不崩溃，继续检查下一个
# 测试: ["CLAUDE.md", "imaginary.txt", "python/01_basics.py"]

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
file_list = ["CLAUDE.md", "imaginary.txt", "python/01_basics.py"]
import os
def check_files(file_list):
    for fname in file_list:
        if os.path.exists(fname):
            print(f"✅ {fname}: 存在")
        else:
            print(f"⚠️ {fname}: 缺失")
check_files(file_list)



print("\n")

# ── 练习 3 ──
# 给 calc_psi 函数再加一个检查：Ce 必须 > 1（因为 log10(1)=0，log10(<1)为负）
# 写新函数 calc_psi_safe，如果 Ce <= 1 返回 -1 而不是崩溃

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
def calc_psi_safe(Q_mg_g, Ce):
    import math
    if Q_mg_g <= 0:
        return -1
    if Ce <= 1:
        return -1
    Q_mg_kg = Q_mg_g * 1000
    return Q_mg_kg / math.log10(Ce)
print(calc_psi_safe(-1, 0.5))   # 正常输入

print("\n完成！下一步：07_strings.py")
