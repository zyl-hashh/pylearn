"""
Python 入门第 4 课 —— 字典 dict

字典 = 标签本，每个数据都贴了名字，用名字找数据。
列表用数字下标[0][1]找，字典用任意名字["EPC0"]找。

科研里字典超级常见：一个样品的信息（名字、EPC0、PSI、Qmax...）
用字典比用六个列表清爽太多。
"""

# ═══════════════════════════════════════════════════════════
# 1. 创建字典 — 用花括号 {}，格式是 {键: 值}
# ═══════════════════════════════════════════════════════════

# 一个样品就是一个字典：
wa1 = {
    "name": "WA1",
    "EPC0": 0.032,      # 键是字符串 "EPC0"，值是数字
    "PSI": 533.5,
    "Qmax": 0.623,
    "SRP": 0.045,
}
# 键可以用引号，值什么类型都行（数字、字符串、列表...）

# 取值：字典名["键名"]
print(f"样品: {wa1['name']}")
print(f"EPC0: {wa1['EPC0']} mg/L")
print(f"PSI:  {wa1['PSI']} mg/kg")
print(f"Qmax: {wa1['Qmax']} mg/g")

# 新增/修改：直接赋值
wa1["location"] = "万安大坝"       # 新键，自动加上
wa1["PSI"] = 540.0                # 已有键，覆盖旧值
print(f"\n修改后: {wa1}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 遍历字典
# ═══════════════════════════════════════════════════════════

print("遍历所有键值对：")
for key, value in wa1.items():   # .items() = 拿出每一对 (键, 值)
    print(f"  {key}: {value}")

print("\n只看键：")
for key in wa1.keys():           # .keys() = 所有键
    print(f"  {key}")

print("\n只看值：")
for value in wa1.values():       # .values() = 所有值
    print(f"  {value}")

# 安全取值：用 .get()，键不存在时返回默认值不报错
print(f"\nlocation: {wa1.get('location', '未记录')}")
print(f"depth: {wa1.get('depth', '未记录')}")   # 没这个键 → 默认值

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 3. 字典列表 — 你科研里的核心数据结构
# ═══════════════════════════════════════════════════════════

# 8 个样品 = 8 个字典装在一个列表里
samples = [
    {"name": "WA1", "PSI": 533.5, "Qmax": 0.623, "EPC0": 0.032},
    {"name": "WA2", "PSI": 517.6, "Qmax": 0.587, "EPC0": 0.045},
    {"name": "WA3", "PSI": 488.9, "Qmax": 0.541, "EPC0": 0.028},
    {"name": "WA4", "PSI": 475.1, "Qmax": 0.512, "EPC0": 0.051},
    {"name": "WA5", "PSI": 521.1, "Qmax": 0.598, "EPC0": 0.039},
    {"name": "WA6", "PSI": 467.5, "Qmax": 0.503, "EPC0": 0.047},
    {"name": "WA7", "PSI": 524.0, "Qmax": 0.601, "EPC0": 0.034},
    {"name": "WA8", "PSI": 539.6, "Qmax": 0.635, "EPC0": 0.041},
]

# 这才叫科研的数据结构！所有信息在一起，一目了然
print("全部样品：")
for s in samples:
    print(f"  {s['name']}: PSI={s['PSI']}, Qmax={s['Qmax']}, EPC0={s['EPC0']}")

# 查找 PSI 最高的是哪个
best = max(samples, key=lambda s: s["PSI"])    # lambda 第 11 节讲
print(f"\nPSI 最高: {best['name']} ({best['PSI']} mg/kg)")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 4. 统计字典 — 用来记计数、分组求和
# ═══════════════════════════════════════════════════════════

# 有了字典，统计变得超简单。比如统计 PSI 等级分布：
levels = {"高": 0, "中": 0, "低": 0}

for s in samples:
    if s["PSI"] > 520:
        levels["高"] += 1
    elif s["PSI"] > 480:
        levels["中"] += 1
    else:
        levels["低"] += 1

print(f"PSI 等级分布: {levels}")   # {'高': 4, '中': 2, '低': 2}

# 按地点分组的平均 Qmax（假设 WA1-3 是坝前，WA4-8 是坝后）
grouped = {"坝前": [], "坝后": []}
for i, s in enumerate(samples):
    if i < 3:
        grouped["坝前"].append(s["Qmax"])
    else:
        grouped["坝后"].append(s["Qmax"])

for loc, vals in grouped.items():
    print(f"{loc}: 平均 Qmax = {sum(vals)/len(vals):.3f}")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 把下面的三个列表改成一个字典列表（像上面 samples 那样）
names = ["S1", "S2", "S3"]
temps = [24.5, 26.1, 22.8]
phs   = [7.2, 7.8, 6.9]
# 要求：创建 stations = [{...}, {...}, {...}]，每个字典有 name/temp/pH
# 然后遍历打印 "站点 X: 温度=Y°C, pH=Z"

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓



stations = [{"name":n,"temp":t,"ph":p} for n,t,p in zip (names,temps,phs)]
for s in stations:
    print(f"站点 {s['name']}: 温度={s['temp']}°C,pH={s['ph']}")
print("\n")
print(stations)
# ── 练习 2 ──
# 用上面 samples 列表，统计 EPC0 > 0.04 的样品有哪些
# 打印它们的名字和 EPC0 值

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
for s in samples:
    if s['EPC0'] >0.04:    
        print(f"{s["name"]}:EPC0={s['EPC0']}")


print("\n")

# ── 练习 3 ──
# 创建一个统计字典 counts，统计 samples 中 PSI > 500 和 PSI <= 500 各有多少个
# 不能用 if/elif/else，写完试试

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
counts = {"PSI > 500": 0, "PSI <= 500": 0}
for s in samples:
    if s["PSI"] > 500:
        counts["PSI > 500"] += 1
    else:
        counts["PSI <= 500"] += 1
print(counts)

print("\n完成！下一步：05_file_io.py")
