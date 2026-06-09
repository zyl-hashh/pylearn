"""
Python 第 29 课 —— 环境管理与依赖锁定

═══════════════════════════════════════════════════════════
情景
═══════════════════════════════════════════════════════════

你把代码发给导师，导师运行 python main.py：
  ModuleNotFoundError: No module named 'pandas'
  ModuleNotFoundError: No module named 'openpyxl'
  ModuleNotFoundError: No module named 'scipy'

"你这代码到底需要装哪些包？什么版本？"

requirements.txt 就是回答这个问题的文件。

═══════════════════════════════════════════════════════════
本节学习
═══════════════════════════════════════════════════════════
  1. pip freeze  → 导出所有已装包的列表
  2. requirements.txt → 依赖声明文件（项目的"配料表"）
  3. pip install -r requirements.txt → 一键安装所有依赖
"""

print("=" * 60)
print("环境管理实操")
print("=" * 60)


# ═══════════════════════════════════════════════════════════
# 第 1 步：pip freeze — 看看你装了什么
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 1 步：pip freeze — 导出环境快照                         │
└─────────────────────────────────────────────────────────┘

在终端里（先用 pip install pandas openpyxl matplotlib 装几个包）：

  pip freeze

你会看到一大堆输出：
  pandas==2.0.3
  numpy==1.26.4
  python-dateutil==2.8.2
  ...

每一行格式：包名==版本号
注意：pip freeze 会列出所有依赖（包括 numpy 是 pandas 的依赖），
不是只有你手动装的。

把输出重定向到文件：
  pip freeze > requirements.txt

这样 requirements.txt 里就是当前环境的所有包了。
""")


# ═══════════════════════════════════════════════════════════
# 第 2 步：一键安装 — pip install -r
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 2 步：pip install -r — 一键安装所有依赖                  │
└─────────────────────────────────────────────────────────┘

clone 了你的代码后，同事只需要一行命令：

  pip install -r requirements.txt

pip 就会逐行读取 requirements.txt，把每个包安装好。
这就是"环境复现"——从零到和你的环境一模一样，一行命令。

练习（在终端跑）：
  1. 激活虚拟环境（如果没激活的话）
  2. pip freeze > requirements.txt
  3. 打开 requirements.txt，看看有哪些包
  4. 新建另一个虚拟环境（比如叫 venv2），激活它
  5. pip install -r requirements.txt
  6. 检查两个环境的 pip list 是否一样
""")


# ═══════════════════════════════════════════════════════════
# 第 3 步：手写精简 requirements.txt
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 3 步：精简版 requirements.txt（推荐）                    │
└─────────────────────────────────────────────────────────┘

pip freeze 的问题：它导出了所有间接依赖。
比如你只装了 pandas，但它还把 numpy、python-dateutil、
pytz、six 全写进去了——这些都是 pandas 依赖的包，
不是你显式装的。

更好的做法：只写你直接 import 的包：

  # requirements.txt（手写版）
  pandas>=2.0.0,<3.0.0    # 最低 2.0，不能到 3.0
  matplotlib>=3.8.0
  openpyxl>=3.1.0
  scipy>=1.11.0

版本号语法：
  ==       → 精确等于     pandas==2.0.3
  >=       → 大于等于     pandas>=2.0.0
  >=,<     → 范围限定     pandas>=2.0.0,<3.0.0
  ~=       → 兼容版本     pandas~=2.0.3（等于 >=2.0.3, <2.1）

为什么用 >= 而不是 == ？
  用 == 锁定死版本，别人的环境可能装不上（特别是跨平台）
  用 >= 给一定灵活性，保证最小版本即可
""")


# ═══════════════════════════════════════════════════════════
# 第 4 步：你的项目的标准结构
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 4 步：一个标准 Python 项目的文件结构                     │
└─────────────────────────────────────────────────────────┘

  myproject/
  ├── venv/              ← 虚拟环境（不要提交到 Git！）
  ├── .gitignore         ← 告诉 Git 忽略 venv/ 和 __pycache__/
  ├── requirements.txt   ← 依赖清单
  ├── README.md          ← 项目说明 + 怎么运行
  ├── main.py            ← 入口脚本
  ├── utils.py           ← 工具函数
  └── data/              ← 数据文件夹

.gitignore 至少包含这些：
  venv/
  __pycache__/
  *.pyc
  .vscode/
  node_modules/

这样 clone 你项目的人只需要：
  git clone 你的仓库
  cd 你的仓库
  python -m venv venv
  source venv/Scripts/activate   # 或 venv\\Scripts\\activate
  pip install -r requirements.txt
  python main.py
""")


# ═══════════════════════════════════════════════════════════
# 练习
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习")
print("=" * 50 + "\n")

print("""
1. 把你工作区里 scripts/ 文件夹中任意一个 plot_*.py 需要的包
   列出来，写成一个 requirements.txt
   （比如 pandas, matplotlib, numpy, scipy, openpyxl）

2. 确认这些包你都已经装过了（pip list 查看）

3. 把 requirements.txt 保存到 python/ 文件夹

4. 试试这个完整流程（模拟别人 clone 你的项目）：
   a. 新开一个终端
   b. 创建虚拟环境 python -m venv test_env
   c. 激活
   d. pip install -r requirements.txt
   e. deactivate
   f. 删除 test_env
""")


# ═══════════════════════════════════════════════════════════
# 复习练习（08-09 课：pathlib + 推导式）
# 难度：⭐⭐⭐（多知识点组合）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：扫描项目找出所有 import 语句")
print("=" * 50)

print("""
═══════════════ 分步引导 ═══════════════

第 1 步：用 pathlib 遍历 python/ 文件夹
  from pathlib import Path
  py_dir = Path.home() / "Desktop" / "vscode" / "python"
  for f in py_dir.rglob("*.py"):
      print(f.name)                  # 先确认能列出所有 .py

第 2 步：读一个文件，提取 import 行
  content = f.read_text(encoding="utf-8")
  for line in content.splitlines():
      if line.startswith("import ") or line.startswith("from "):
          print(line.strip())

第 3 步：用集合去重（因为同一个包可能在多个文件出现）
  imports = set()   # 创建空集合
  imports.add("pandas")
  imports.add("pandas")  # 重复的不会加进去
  print(imports)           # 只有 {'pandas'}

第 4 步：筛选第三方库（排除 Python 标准库）
  标准库（无需安装的）：os, sys, math, re, pathlib, json, unittest 等
  第三方库（需要 pip install 的）：pandas, matplotlib, numpy, scipy 等
  简单办法：建一个"排除名单"来过滤

══════════════════════════════

现在从第 1 步开始，一步步写。卡住了看上面的引导。
""")
print("=" * 50 + "\n")

# ↓↓↓ 你的代码 ↓↓↓
from pathlib import Path
py_dir=Path.home() /'Desktop'/'vscode'/'python'
pydoc=[p for p in py_dir.rglob('*.py')]
print(pydoc)
sc=[]
for f in pydoc:
    with open(f,'r',encoding='utf-8') as file:
        for line in file:
            if line.startswith('import') or line.startswith('from'):
                sc.append(line.strip())
nesc=list(set(sc))
print(nesc)
qc=['os', 'sys', 'math', 're', 'pathlib', 'json', 'unittest']
ac=list(set(nesc)-set(qc))
print(ac)

from pathlib import Path

py_dir = Path.home() / 'Desktop' / 'vscode' / 'python'
sc = []
for f in py_dir.rglob('*.py'):
    content = f.read_text(encoding='utf-8')
    for line in content.splitlines():
        if line.startswith('import ') or line.startswith('from '):
            sc.append(line.strip())

# 去重
nesc = list(set(sc))
print("所有 import 语句:")
for i in sorted(nesc):
    print(f"  {i}")

# 排除标准库
stdlib = {'os', 'sys', 'math', 're', 'pathlib', 'json', 'unittest', 'time'}
third_party = [i for i in nesc if i not in stdlib]
print(f"\n第三方库相关的 import:")
for i in third_party:
    print(f"  {i}")
# ═══════════════════════════════════════════════════════════
# 就业前瞻：Docker — 虚拟环境的终极版
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】Docker — 连操作系统一起打包")
print("=" * 50)
print("""
虚拟环境只隔离了 Python 包。但如果：
  - 同事用 Windows，服务器是 Linux
  - 项目需要特定版本的 C 库（比如 GDAL 做地理信息）
  - 你需要 PostgreSQL 数据库 + Redis 缓存同时跑

这时候虚拟环境不够用了。Docker 上场——它把整个操作系统环境
（OS + Python + 库 + 数据库 + 一切）打包成一个"镜像"。

你现在不需要学 Docker。记住一句话：
  虚拟环境 → 隔离 Python 包
  Docker   → 隔离整台机器

等你学完 Web 开发、部署到服务器的时候，再回来学 Docker。
那时候你会明白为什么它叫"集装箱"——一套环境，到处运行。
""")
