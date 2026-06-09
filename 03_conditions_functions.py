"""
Python 入门第 3 课 —— 条件判断与函数

if/elif/else = 根据条件决定做什么
def = 把一段代码打包，以后重复用

先跑一遍看效果，再去做最下面的练习题。
"""

# ═══════════════════════════════════════════════════════════
# 1. if / elif / else — 条件判断
# ═══════════════════════════════════════════════════════════

epc0 = 0.045
srp = 0.032

# 比较运算符：== 等于, != 不等于, > < >= <=
print(f"EPC0 = {epc0}, SRP = {srp}")

if epc0 > srp:
    print("  EPC0 > SRP → 底泥释放磷到上覆水")     # 条件成立走这
elif epc0 < srp:
    print("  EPC0 < SRP → 上覆水中的磷被底泥吸附")   # 第二个条件
else:
    print("  EPC0 = SRP → 平衡状态")              # 都不成立走这

# 你的科研代码里到处都是这种判断：
psi = 520
if psi > 500:
    level = "高"
elif psi > 400:
    level = "中"
else:
    level = "低"
print(f"  PSI = {psi} → {level}吸附能力")

# 多个条件用 and / or：
temp = 25
ph = 7.2
if temp > 20 and ph < 8:     # 同时满足
    print(f"  温度{temp}°C, pH{ph} → 条件合适")
if temp < 10 or ph > 9:       # 满足一个就行
    print(f"  超出适宜范围")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. def — 定义函数，打包重复用的代码
# ═══════════════════════════════════════════════════════════

# 你之前 EPC0 脚本里的 style_ax(ax) 就是函数
# def 函数名(参数):  →  写好之后，每次调用函数名就行

# 例子：定义一个计算吸附量 Q 的函数
def calc_q(C0, Ce, V, m):
    """计算吸附量 Q（mg/g）
    C0 = 初始浓度 (mg/L)
    Ce = 平衡浓度 (mg/L)
    V  = 溶液体积 (L)
    m  = 吸附剂质量 (g)
    """
    Q = (C0 - Ce) * V / m
    return Q    # return = 把计算结果"交出去"

# 调用函数：
q1 = calc_q(C0=75, Ce=33.76, V=0.020, m=1)
q2 = calc_q(75, 34.85, 0.020, 1)     # 不写参数名也行，按顺序传
print(f"Q1 = {q1:.4f} mg/g")
print(f"Q2 = {q2:.4f} mg/g")

# 函数可以有多行、多参数、多个 return：
def rate_psi(psi):
    """给 PSI 值分等级"""
    if psi > 520:
        return "高吸附能力"
    elif psi > 480:
        return "中吸附能力"
    else:
        return "低吸附能力"

print(f"PSI=535 → {rate_psi(535)}")
print(f"PSI=500 → {rate_psi(500)}")
print(f"PSI=460 → {rate_psi(460)}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 函数 + 循环 = 批量处理
# ═══════════════════════════════════════════════════════════

# 这正是你科研里每时每刻都在做的事！
samples = ["WA1","WA2","WA3","WA4","WA5","WA6","WA7","WA8"]
ce_values = [33.76, 34.85, 36.84, 37.73, 34.95, 38.03, 35.85, 34.46]

print("批量计算 Q 值：")
for name, ce in zip(samples, ce_values):
    q = calc_q(75, ce, 0.020, 1)
    print(f"  {name}: Ce={ce}, Q={q:.4f} mg/g")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 几个常用技巧
# ═══════════════════════════════════════════════════════════

# 列表去重：
values = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(values))     # set() 自动去重
print("去重后:", unique)

# 统计元素出现次数：
text = "WA1,WA2,WA1,WA3,WA2,WA1"
count_wa1 = text.count("WA1")
print(f"WA1 出现了 {count_wa1} 次")

# in 判断元素在不在：
samples_list = ["WA1", "WA2", "WA3"]
print("WA2 在列表里吗?", "WA2" in samples_list)
print("WA5 在列表里吗?", "WA5" in samples_list)


# ═══════════════════════════════════════════════════════════
# 练习题（必须自己敲！）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题 — 在下面空白处自己写代码")
print("=" * 50 + "\n")

# 数据准备：
samples = ["WA1", "WA2", "WA3", "WA4", "WA5", "WA6", "WA7", "WA8"]
ce = [33.76, 34.85, 36.84, 37.73, 34.95, 38.03, 35.85, 34.46]
qmax = [0.623, 0.587, 0.541, 0.512, 0.598, 0.503, 0.601, 0.635]

# ── 练习 1 ──
# 写一个函数 calc_psi(Q_mg_per_g, Ce)，计算 PSI = Q(mg/kg) / log10(Ce)
# 注意：Q 的单位是 mg/g，要先 ×1000 转成 mg/kg
# 提示：需要 import math，用 math.log10()
# 然后调用函数，算 WA3 的 PSI（WA3 的 Ce=36.84，Q=0.541）

print("练习 1:")
import math
import numpy as np  

# ↓↓↓ 在下面写你的代码 ↓↓↓
def calc_psi(Q_mg_per_g, Ce):
    Q_mg_per_kg = Q_mg_per_g * 1000
    psi = Q_mg_per_kg / math.log10(Ce)
    return psi
wa3_q = qmax[2]  # WA3 的 Q
wa3_ce = ce[2]   # WA3 的 Ce
wa3_psi = calc_psi(wa3_q, wa3_ce)
print(f"WA3 的 PSI = {wa3_psi:.4f}")
print(f"WA3 的 PSI = {wa3_psi:.4f}")
# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n")

# ── 练习 2 ──
# 写一个函数 classify_qmax(q)，把 Qmax 分三类：
#   > 0.60  → "高"
#   0.55~0.60 → "中"
#   < 0.55 → "低"
# 然后用循环对 8 个样品批量评判，打印 "{样品名}: Qmax={值} → {等级}"

print("练习 2:")
# ↓↓↓ 在下面写你的代码 ↓↓↓
def classify_qmax(q):
     if q > 0.60:
         return "高"
     elif q > 0.55 and q <0.6:
         return "中"
     else:
         return"低"
for name,q in zip(samples,qmax):
    rate=classify_qmax(q)
    print(f"{name}: Qmax = {q} → {rate}")



# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n")

# ── 练习 3（挑战）──
# 统计 8 个样品中 Qmax 高/中/低各有多少个
# 提示：可以用三个计数器变量，遍历时 += 1

print("练习 3 (挑战):")
# ↓↓↓ 在下面写你的代码 ↓↓↓





# ↑↑↑ 写完运行看结果 ↑↑↑

print("\n完成！你已经学会了：变量、列表、循环、条件、函数")
print("这五个东西加起来，能写 80% 的科研数据处理代码了")
rate_nu = [classify_qmax(q) for q in qmax]
high = rate_nu.count("高")
mid = rate_nu.count("中")
low = rate_nu.count("低")
print(f"高: {high} 个, 中: {mid} 个, 低: {low} 个")