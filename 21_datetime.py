"""
Python 第 21 课 —— 时间处理 datetime

科研里的时间序列数据（水质监测、实验记录）绕不开时间处理。
学会 datetime 后，你可以自动给文件名加日期、算时间差、按月汇总。
"""

from datetime import datetime, timedelta
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 1. 获取当前时间、创建指定时间
# ═══════════════════════════════════════════════════════════

now = datetime.now()
print(f"现在: {now}")
print(f"  年: {now.year}")
print(f"  月: {now.month}")
print(f"  日: {now.day}")
print(f"  时: {now.hour}:{now.minute}:{now.second}")

# 创建指定日期
sample_date = datetime(2026, 3, 15, 14, 30)   # 2026-03-15 14:30
print(f"\n指定: {sample_date}")

# ═══════════════════════════════════════════════════════════
# 2. 格式化 — strftime 和 strptime
# ═══════════════════════════════════════════════════════════

# datetime → 字符串（格式化输出）
print(f"\n格式 1: {now.strftime('%Y-%m-%d')}")          # 2026-05-27
print(f"格式 2: {now.strftime('%Y年%m月%d日 %H:%M')}")  # 2026年05月27日 10:30

# 字符串 → datetime（解析）
raw = "2026-05-21 09:30"
parsed = datetime.strptime(raw, "%Y-%m-%d %H:%M")
print(f"解析 '{raw}' → {parsed}, 星期 {parsed.weekday()+1}")

# 常用格式化代码
#   %Y = 4位年  %m = 月  %d = 日  %H = 时  %M = 分  %S = 秒
#   %A = 星期几英文  %B = 月份英文

# ═══════════════════════════════════════════════════════════
# 3. 时间运算 — timedelta
# ═══════════════════════════════════════════════════════════

# 时间差：昨天、下周、三天前
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
three_days_ago = now - timedelta(days=3, hours=5)

print(f"\n昨天: {yesterday.strftime('%Y-%m-%d')}")
print(f"下周: {next_week.strftime('%Y-%m-%d')}")

# 计算间隔
experiment_start = datetime(2026, 5, 1)
experiment_end = datetime(2026, 5, 27)
delta = experiment_end - experiment_start
print(f"实验持续天数: {delta.days} 天")

# ═══════════════════════════════════════════════════════════
# 4. 实战：自动给文件名加时间戳
# ═══════════════════════════════════════════════════════════

def make_filename(prefix, ext=".csv"):
    """根据当前时间生成文件名，如: PSI_报告_20260527_1430.csv"""
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    return f"{prefix}_{ts}{ext}"

print(f"\n自动生成文件名: {make_filename('PSI_报告')}")
print(f"自动生成文件名: {make_filename('水质数据', '.xlsx')}")

# 按季度判断
def get_quarter(d):
    return (d.month - 1) // 3 + 1   # 1-3月→Q1, 4-6→Q2...

print(f"当前季度: Q{get_quarter(now)}")


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 打印 7 天前和 30 天后的日期，格式: YYYY年MM月DD日

print("练习 1:")
# ↓↓↓
sevens_days_ago = datetime.now() - timedelta(days=7)
thirty_days_later = datetime.now() + timedelta(days=30)

print(f"7天前: {sevens_days_ago.strftime('%Y年%m月%d日')}")
print(f"30天后: {thirty_days_later.strftime('%Y年%m月%d日')}")

print("\n")

# ── 练习 2 ──
# 写函数 days_between(d1_str, d2_str)，输入 "2026-05-01" 和 "2026-06-15"
# 返回间隔天数

print("练习 2:")
# ↓↓↓
def days_between(d1_str, d2_str):
    d1 = datetime.strptime(d1_str, "%Y-%m-%d")
    d2 = datetime.strptime(d2_str, "%Y-%m-%d")
    return abs((d2 - d1).days)
days = days_between("2026-05-01", "2026-06-15")
print(f"间隔天数: {days} 天")

# ═══════════════════════════════════════════════════════════
# 复习练习（08-09 课：pathlib + 推导式）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：用 pathlib 列出桌面 python 文件夹")
print("然后字典推导式生成 {文件名: 字节大小} 的字典")
print("=" * 50 + "\n")

# ↓↓↓ 你的代码 ↓↓↓
from pathlib import Path
p = Path.home() / "Desktop" / "python"
for f in p.glob('*.py'):
    print(f"{f.name}")
dir={f.name: f.stat().st_size for f in p.glob('*.py')}
print(dir)

# ═══════════════════════════════════════════════════════════
# 就业前瞻：SQL 是什么
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】SQL — 数据库的语言")
print("=" * 50)
print("""
你现在的数据存在 Excel 里，打开→筛选→手动整理。
数据库是"超级 Excel 表格"，可以存几百万行，查询 0.01 秒。

SQL = Structured Query Language（结构化查询语言）
它就是跟数据库"对话"的语言。把你熟悉的 Excel 操作翻译成 SQL：

  Excel: 筛选 TP > 1000 的行
  SQL:   SELECT * FROM sediment WHERE TP > 1000

  Excel: 按深度分组求均值
  SQL:   SELECT depth, AVG(TP) FROM sediment GROUP BY depth

  Excel: VLOOKUP 两张表
  SQL:   SELECT * FROM table_a JOIN table_b ON a.ID = b.ID

你现在学 pandas 的 df.query()、df.groupby()、pd.merge()，本质上就是在学 SQL。
pandas 熟练了，SQL 学起来飞快——语法不同，逻辑一样。

一句话：Excel 管几百行，数据库管几百万行，SQL 是中间的语言。
""")
