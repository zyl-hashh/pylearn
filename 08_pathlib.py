"""
Python 入门第 8 课 —— 路径操作 pathlib

以前你用 os.path.join / os.path.exists，现在学更现代的 pathlib。
一个 Path 对象既能拼路径，也能读文件、建文件夹、看大小。
学会后你再也不用硬编码 C:\Users\Nicholas\... 了。
"""

from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 1. 创建 Path 对象
# ═══════════════════════════════════════════════════════════

# Path("路径") 创建一个路径对象，比字符串多了很多功能
p = Path("C:/Users/Nicholas/Desktop/赣江数据/WA.xlsx")
print(f"完整路径: {p}")
print(f"父目录:   {p.parent}")      # 文件所在的文件夹
print(f"文件名:   {p.name}")         # 纯文件名 WA.xlsx
print(f"后缀:     {p.suffix}")       # .xlsx
print(f"不带后缀: {p.stem}")         # WA

# 路径拼接——比 os.path.join 更直观，直接用 /
data_dir = Path("C:/Users/Nicholas/Desktop/赣江数据")
wa_path = data_dir / "WA.xlsx"            # / 自动拼路径！
ads_path = data_dir / "吸附实验" / "吸附实验.xlsx"
print(f"\n拼接结果: {wa_path}")
print(f"拼接结果: {ads_path}")

# 相对路径和绝对路径
here = Path(".")                           # . = 当前目录
here_abs = here.resolve()                  # .resolve() = 转成绝对路径
print(f"\n当前目录: {here_abs}")

# 用户目录（跨平台！Win/Mac/Linux 都行）
home = Path.home()
print(f"用户目录: {home}")                 # C:\Users\Nicholas
print(f"桌面: {home / 'Desktop'}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 2. 文件和文件夹的判断
# ═══════════════════════════════════════════════════════════

workspace = Path("C:/Users/Nicholas/Desktop/vscode")

print(f"工作区存在吗? {workspace.exists()}")      # True/False
print(f"是文件夹吗?   {workspace.is_dir()}")
# print(f"是文件吗?     {workspace.is_file()}")   # False，它是文件夹

# 遍历目录（这个超级有用！）
print("\n工作区里的文件和文件夹:")
for item in workspace.iterdir():
    item_type = "📁" if item.is_dir() else "📄"
    print(f"  {item_type} {item.name}")

# 只找特定后缀：
print("\n工作区里的 .py 文件:")
for py_file in workspace.rglob("*.py"):   # rglob = 递归搜索（含子文件夹）
    print(f"  {py_file.name}")


# ═══════════════════════════════════════════════════════════
# 3. 读文件和写文件 — Path 自带的方法
# ═══════════════════════════════════════════════════════════

out = Path("lesson08_demo.txt")

# 写 — write_text() 一行搞定！
out.write_text("Path 写文件太方便了\n第二行\n第三行", encoding="utf-8")
print(f"\n已写入: {out}")

# 读 — read_text() 一行搞定！
content = out.read_text(encoding="utf-8")
print(f"读出内容:\n{content}")

# 读成行列表：
lines = out.read_text(encoding="utf-8").splitlines()
print(f"共 {len(lines)} 行")

# 建文件夹
new_dir = Path("lesson08_temp")
new_dir.mkdir(exist_ok=True)       # exist_ok=True = 已存在不报错
print(f"文件夹已存在/创建: {new_dir}")


# ═══════════════════════════════════════════════════════════
# 4. 批量文件重命名 — 实战
# ═══════════════════════════════════════════════════════════

# 假设你有一堆 tif 文件要统一加前缀
# 这个循环说明思路，不真的改你的文件

fake_files = ["WA1_PSI.tif", "WA2_PSI.tif", "WA3_PSI.tif"]
print("\n模拟重命名:")
for fname in fake_files:
    p = Path(fname)
    new_name = p.parent / f"Fig_{p.stem}{p.suffix}"
    # 真实场景去掉注释就用: p.rename(new_name)
    print(f"  {fname} → {new_name}")

print("──────────────")


# ═══════════════════════════════════════════════════════════
# 练习题
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("练习题")
print("=" * 50 + "\n")

# ── 练习 1 ──
# 用 pathlib 列出你桌面上所有 .docx 文件
# 提示: Path.home() / "Desktop" 然后用 .glob("*.docx")

print("练习 1:")
# ↓↓↓ 写你的代码 ↓↓↓
from pathlib import Path
p=Path.home() / "Desktop"
for pt in p.glob("*.docx"):
    print(f"{pt.name}")


print("\n")

# ── 练习 2 ──
# 在桌面 python 文件夹里创建一个文件 lesson08_test.txt
# 写入三行内容，然后用 read_text 读出来打印

print("练习 2:")
# ↓↓↓ 写你的代码 ↓↓↓
from pathlib import Path
p = Path.home() / "Desktop"/ "Python"/ "lesson08_test.txt"
p.write_text("1\n2\n3",encoding="utf-8")
print(f"\n已写入: {p}")
content = p.read_text(encoding="utf-8")
for i,n in enumerate(content.splitlines()):
    print(f"第{i+1}行: {n}")


print("\n")

# ── 练习 3 ──
# 写一个函数 find_files(directory, suffix)
# 返回指定目录下所有指定后缀的文件列表（用 rglob）

print("练习 3:")
# ↓↓↓ 写你的代码 ↓↓↓
from pathlib import Path

def find_files(directory, suffix):
    dir_path = Path(directory)
    if  not dir_path.exists():
        return[]
    return list(dir_path.rglob(f"*{suffix}"))


for f in find_files(Path.home() / "Desktop" / "vscode" / "python", ".py"):
    print(f"{f.name}")
print("\n完成！下一步：09_comprehensions.py")
