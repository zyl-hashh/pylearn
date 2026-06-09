"""
Python 第 27 课 —— GitHub：你的代码简历

═══════════════════════════════════════════════════════════
GitHub 是什么
═══════════════════════════════════════════════════════════

Git 管理的是你电脑上的代码。GitHub 是把这份代码放到网上，
让全世界都能看到、协作、下载。

类比：
  Git      = 你电脑上的 Word，记录每次修改
  GitHub   = 把 Word 文档传到百度网盘分享
  GitLab   = 公司内部的"GitHub"（很多公司用）
  Gitee    = 国内的 GitHub（码云，访问更快）

═══════════════════════════════════════════════════════════
核心概念（5 分钟看懂）
═══════════════════════════════════════════════════════════

 本地仓库 (local repo)
   → 你电脑上的那个文件夹（比如上一节的 git_demo）
   → git add/commit 都在本地

 远程仓库 (remote repo)
   → GitHub 上的那个仓库
   → 你和同事共享的"中心仓库"

 push（推送）
   → 把本地的 commit 上传到 GitHub
   → git push = "我写完了，发上去"

 pull（拉取）
   → 把 GitHub 上的最新版本下载到本地
   → git pull = "看看别人写了什么"

 clone（克隆）
   → 把 GitHub 上的仓库整个下载到你电脑
   → git clone 网址 = "我要这个项目的完整代码+全部历史"

 Pull Request（PR / 拉取请求）
   → 你改了代码，请求项目负责人审核并合并进去
   → 开源社区协作的核心机制

═══════════════════════════════════════════════════════════
先决条件
═══════════════════════════════════════════════════════════
你需要：
  1. 注册 GitHub 账号（https://github.com，免费）
  2. 在 GitHub 上创建一个空仓库（New Repository）
     - Repository name: python-learning
     - 勾选 Public（公开）或 Private（私有）
     - 不要勾选 "Add a README file"（我们要从本地推上去）
  3. 记下仓库地址：https://github.com/你的用户名/python-learning.git
"""

print("=" * 60)
print("GitHub 实操 — 请打开 Git Bash，按步骤操作")
print("=" * 60)


# ═══════════════════════════════════════════════════════════
# 第 1 步：把本地仓库连接到 GitHub — git remote add
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 1 步：连接本地仓库和 GitHub                             │
└─────────────────────────────────────────────────────────┘

确保你在上一节的 git_demo 目录里，然后：

  git remote add origin https://github.com/zyl-hashh/Python-learning.git
  #                    ↑         ↑
  #                    │         └── GitHub 仓库地址
  #                    └── 给远程仓库起个名字（origin 是惯例）

  git remote -v     # 查看已连接的远程仓库

你会看到:
  origin  https://github.com/... (fetch)
  origin  https://github.com/... (push)

意思：本地仓库现在知道"origin"指向那个 GitHub 地址了。
- fetch = 从哪下载
- push = 往哪上传
""")


# ═══════════════════════════════════════════════════════════
# 第 2 步：把代码推上去 — git push
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 2 步：git push — 把本地代码上传到 GitHub                │
└─────────────────────────────────────────────────────────┘

  git push -u origin main
  #         ↑  ↑      ↑
  #         │  │      └── 推送到哪个分支（main 是默认主分支）
  #         │  └── 远程仓库名
  #         └── -u = 记住这个对应关系，下次只敲 git push 就行

可能会提示你登录 GitHub——输入用户名和密码（或 token）。

成功后打开 https://github.com/你的用户名/python-learning，
你应该看到 hello.py 和 .gitignore 都在上面了！
""")
#git remote set-url origin git@github.com:zyl-hashh/pylearn.git

# ═══════════════════════════════════════════════════════════
# 第 3 步：从 GitHub 拉取 — git pull
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 3 步：模拟协作 — 在 GitHub 网页上改文件                  │
└─────────────────────────────────────────────────────────┘

1. 在 GitHub 网页上打开你的 python-learning 仓库
2. 点击 hello.py → 点右上角铅笔图标（Edit this file）
3. 加一行 "print('这行是在GitHub上添加的')"
4. 往下翻，点绿色的 "Commit changes" 按钮
5. 现在 GitHub 上的代码比你的本地代码新了！

回到 Git Bash:
  git pull origin main              # 把 GitHub 的更新拉下来
  cat hello.py                      # 看到新增的那一行了！

git pull 的实际操作 = git fetch（下载） + git merge（合并）
""")


# ═══════════════════════════════════════════════════════════
# 第 4 步：克隆别人的项目 — git clone
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 第 4 步：git clone — 一键下载整个项目                       │
└─────────────────────────────────────────────────────────┘

回到桌面：
  cd ~/Desktop
  git clone https://github.com/你的用户名/python-learning.git python-learning-copy
  #                                                               ↑
  #                                     给下载的文件夹起个名字（不写就默认用仓库名）

  cd python-learning-copy
  git log                  # 所有历史记录都在！clone 下载的是整个仓库的历史

clone 和"下载 ZIP 压缩包"的区别：
  ZIP   → 只有最新版本的文件，没有历史
  clone → 文件 + 全部历史快照 + 分支 + 标签，完整仓库
""")


# ═══════════════════════════════════════════════════════════
# 第 5 步：日常工作流 — 这就是你未来的每一天
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 每日工作流（背下来，这是程序员的标准操作）                   │
└─────────────────────────────────────────────────────────┘

 早上来：
   git pull                     # 拉最新的代码

 工作时：
   git add 改过的文件            # 加入暂存区
   git commit -m "做了什么"      # 提交（可以多次）
   ...继续写代码...

 下班前：
   git push                     # 推送到 GitHub

 简洁版：
   git pull → 写代码 → git add → git commit → git push

 这就是你以后每一天的标准操作，五步，到退休都这样。
""")


# ═══════════════════════════════════════════════════════════
# 练习
# ═══════════════════════════════════════════════════════════

print("""
┌─────────────────────────────────────────────────────────┐
│ 练习 — 在终端完成                                          │
└─────────────────────────────────────────────────────────┘

1. 注册 GitHub 账号（如果还没有）
2. 创建一个仓库 python-learning
3. 把上一节的 git_demo 文件夹连接到这个仓库
4. push 上去
5. 在 GitHub 网页上修改 README.md，加一些内容
6. 在本地 git pull 拉取更新
7. 在本地新建一个文件 notes.md，写几行学习笔记
8. git add → commit → push 推上去
9. 刷新 GitHub 网页，确认 notes.md 出现了

做完后把你 GitHub 仓库的链接给我看看。
""")


# ═══════════════════════════════════════════════════════════
# 复习练习（04-05 课：字典 + 文件读写）
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("复习练习：模拟 git log 解析")
print("""
有一个多行字符串（模拟 git log 输出），每行格式：
  "commit_hash|author|date|message"

要求：
1. 解析成一个字典列表
2. 写入 CSV 文件 git_log.csv
3. 打印每个作者及其提交次数
""")
print("=" * 50 + "\n")

log_data = """abc1234|Nicholas|2026-06-01|修复PSI计算bug
def5678|Alice|2026-06-02|添加EPC0图表
ghi9012|Nicholas|2026-06-02|重构数据读取
jkl3456|Bob|2026-06-03|添加单元测试
mno7890|Nicholas|2026-06-03|更新README"""

# ↓↓↓ 你的代码 ↓↓↓
ka="commit_hash|author|date|message"
key=list(ka.split("|"))
log_data = """abc1234|Nicholas|2026-06-01|修复PSI计算bug
def5678|Alice|2026-06-02|添加EPC0图表
ghi9012|Nicholas|2026-06-02|重构数据读取
jkl3456|Bob|2026-06-03|添加单元测试
mno7890|Nicholas|2026-06-03|更新README"""
lines = log_data.strip().split("\n")
print(lines)
data = [line.split("|") for line in lines]
print(data)
d=[]
for i in data:
  se=dict(zip(key,i))
  d.append(se)
import pandas as pd
df=pd.DataFrame(d)
from pathlib import Path
p=Path.home()/'Desktop'/'python'/'git_log.csv'
df.to_csv(p,index=False)
dica={}
for s in d:
  author=s['author']
  if author in dica:
    dica[author] += 1
  else:
    dica[author] = 1

for author, count in dica.items():
    print(f"{author}:{count}")



# ═══════════════════════════════════════════════════════════
# 就业前瞻：GitHub 是程序员的名片
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("【就业前瞻】你的 GitHub 主页 = 你的第二份简历")
print("=" * 50)
print("""
程序员找工作，HR 不一定看得懂你的项目，但他们会看：
  - GitHub 贡献热力图（绿色格子，越绿越活跃）
  - Star 数和 Follower 数
  - 项目 README 写得好不好
  - 有没有给知名开源项目提过 PR

从现在开始：
  - 每学完一课，把练习代码推到一个 GitHub 仓库
  - 给仓库写一个漂亮的 README（项目简介 + 怎么运行）
  - 坚持 3 个月后，你的热力图就是绿色的，面试时直接展示

一个 GitHub 上 200+ contributions 的应届生，
比一个 GitHub 主页一片空白的"学霸"，拿到 offer 的概率高 5 倍。

原因很简单：代码是给人看的，不是给人猜的。
你会用 Git + GitHub → 你能和别人协作 → 你值这个工资。
""")
