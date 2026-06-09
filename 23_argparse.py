"""
Python 第 23 课 —— 命令行参数 argparse

让你的脚本从"双击运行"变成"在终端里传参数运行"。
比如: python plot.py --sheet water --dpi 300

这就是程序员交付脚本的方式——不是改代码里的变量，而是传参数。
"""

import argparse
import sys

# ═══════════════════════════════════════════════════════════
# 1. 最简 argparse
# ═══════════════════════════════════════════════════════════

# 创建一个"参数解析器"
parser = argparse.ArgumentParser(description="水质数据分析工具")

# 添加参数：
parser.add_argument("--site", type=str, default="万安大坝", help="采样点名称")
parser.add_argument("--year", type=int, default=2026, help="年份")
parser.add_argument("--dpi", type=int, default=600, help="图片分辨率")
parser.add_argument("--verbose", action="store_true", help="是否打印详细信息")
#                    ↑ 不需要值，用了就=True

# 解析（这里只是演示，实际用 parser.parse_args()）
args = parser.parse_args(["--site", "赣江南支", "--year", "2025", "--verbose"])
#                          ↑ 演示！真实代码里不加这个列表

print(f"站点: {args.site}")
print(f"年份: {args.year}")
print(f"DPI:  {args.dpi}")
print(f"详细模式: {args.verbose}")

# ═══════════════════════════════════════════════════════════
# 2. 实战：一个带参数的绘图脚本
# ═══════════════════════════════════════════════════════════

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plot_sample(data, title="数据图", dpi=600, out_dir=None):
    """画折线图，参数全部由外部传入"""
    x = range(1, len(data) + 1)
    fig, ax = plt.subplots()
    ax.plot(x, data, 'o-', color='#2c7bb6')
    ax.set_title(title)
    ax.grid(True, linestyle='--', color='lightgray', alpha=0.7)

    out_dir = out_dir or os.path.expanduser("~/Desktop/python")
    path = os.path.join(out_dir, f"{title}.tif")
    fig.savefig(path, dpi=dpi, format='tiff', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"已保存: {path}")

# 演示调用
plot_sample([533.5, 517.6, 488.9, 475.1], "PSI测试", dpi=300)

# ═══════════════════════════════════════════════════════════
# 3. 标准用法模板
# ═══════════════════════════════════════════════════════════
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="xxx")
#     parser.add_argument("--input", required=True, help="输入文件")
#     parser.add_argument("--output", default="./output", help="输出目录")
#     args = parser.parse_args()
#
#     # 你的主逻辑
#     process(args.input, args.output)
#
# 然后在终端这样跑:
#   python my_script.py --input WA.xlsx --output ./results
#   python my_script.py --input WA.xlsx           # 用默认输出路径
#   python my_script.py --help                    # 看所有可用参数


# ═══════════════════════════════════════════════════════════
# 主课练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("主课练习")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 创建一个 ArgumentParser，接受 --name（字符串）和 --count（整数，默认5）
# 解析 ["--name", "WA1", "--count", "10"] 并打印结果

print("练习 1:")
# ↓↓↓
import argparse
import sys
parser = argparse.ArgumentParser(description="练习用的参数解析器")
parser.add_argument("--name", type=str, required=True, help="名字")
parser.add_argument("--count", type=int, default=5, help="数量")
args = parser.parse_args(["--name", "WA1", "--count", "10"])
print(f"名字: {args.name}")
print(f"数量: {args.count}")


print("\n")

# ── 练习 2 ──
# 写一个完整的 if __name__ == "__main__" 框架
# 接受 --file 和 --sheet 两个参数，打印 "读取 {file} 的 {sheet}"

print("练习 2:")
# ↓↓↓
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="练习用的参数解析器")
    parser.add_argument('--file',type=str,default='data.xlsx',help='输入文件')
    parser.add_argument('--sheet',type=str,default='sheet1',help='表单名称')
    args = parser.parse_args()
    print(f"读取 {args.file} 的 {args.sheet}")


# ═══════════════════════════════════════════════════════════
# 复习练习（14-15 课：pandas 筛选）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：用 pandas 读 sediment sheet，筛选 TP > 1000 的行")
print("打印 ID 和 TP 列")
print("=" * 50 + "\n")

# ↓↓↓ 你的代码 ↓↓↓
import pandas as pd
from pathlib import Path
p=Path.home() / "Desktop" / "赣江数据" / "WA.xlsx"
df=pd.read_excel(p,sheet_name='sediment')
cols=list(df.columns)
cols[4]='TP'
df.columns=cols
high_TP=df[df['TP']>1000]
print(high_TP[['ID','TP']])


# ═══════════════════════════════════════════════════════════
# 就业前瞻：Flask（Web 框架）是什么
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】Flask — 用 Python 写网站")
print("=" * 50)
print("""
你每天上知网、百度学术——浏览器显示的内容，都是后端程序生成的。
Flask 就是 Python 里最简单的后端框架，让你写一个网页服务器。

一个完整的 Flask 应用只有 7 行：

from flask import Flask
  app = Flask(__name__)

  @app.route("/")
  def home():
      return "<h1>万安水库水质监测系统</h1>"

  if __name__ == "__main__":
      app.run()

跑起来之后，浏览器打开 http://localhost:5000，就看到你的网页了。

然后你可以：
  1. 从数据库读数据 → 显示在网页上
  2. 接受用户输入 → 存到数据库
  3. 画图 → 网页上实时显示

这就是"智慧水务平台"的底层原理——一个网页 + 一个数据库 + Python。

一句话：Flask 让你的 Python 代码从"你电脑上跑的脚本"变成"别人浏览器能打开的网站"。
""")
