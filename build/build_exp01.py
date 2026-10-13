# -*- coding: utf-8 -*-
"""构建 EXP01 实验报告 notebook（20244081108_王亨泰_exp01.ipynb）。"""
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

cells = []
def md(src):
    cells.append(new_markdown_cell(src))
def code(src):
    cells.append(new_code_cell(src))

# ===================== 封面 =====================
md("""# 实验报告01：Python基础与数据处理入门

- **学号**：20244081108
- **姓名**：王亨泰
- **环境**：独立 conda 虚拟环境 `pyda`（Python 3.11 + Jupyter），未使用 base 环境

> 本 Notebook 已按顺序运行；提交前重启内核并运行全部代码，无依赖旧变量、无路径错误。""")

# ===================== 第一个代码框 =====================
md("## 一、实验环境与提交要求\n### 1.1 第一个代码框：身份与环境记录")
code('''import os, uuid, hashlib, platform, getpass

# ===== 1. 填写学号 =====
STUDENT_ID = 20244081108  # 修改为自己的学号

# ===== 2. 打印 conda 环境 =====
CONDA_ENV = os.environ.get("CONDA_DEFAULT_ENV", "base")
print(f"[Conda 环境] {CONDA_ENV}")

# ===== 3. 机器指纹（绑定当前电脑） =====
MACHINE_FP = hashlib.sha256(
    f"{platform.node()} | {platform.machine()} | {platform.system()} | {uuid.getnode()}".encode()
).hexdigest()[:16]

# ===== 4. 生成唯一 ID =====
RUN_ID = f"{STUDENT_ID} - {MACHINE_FP}"
print(f"[学号] {STUDENT_ID}")
print(f"[机器指纹] {MACHINE_FP}")
print(f"[RUN_ID] {RUN_ID}")''')

# ===================== 实验1 =====================
md("""---
## 二、实验内容与过程
## 实验1：基本运算、数据类型与字符串

### 任务1.1　基本运算符
分别计算 `8 / 3`、`8 // 3`、`8 % 3` 和 `2 ** 7`，输出结果及其类型。""")
code('''vals = {
    "8 / 3 (除法)": 8 / 3,
    "8 // 3 (整除)": 8 // 3,
    "8 % 3 (取余)": 8 % 3,
    "2 ** 7 (幂)": 2 ** 7,
}
for expr, v in vals.items():
    print(f"{expr:18s} = {v!r:12}  类型={type(v).__name__}")

print("""
运算符含义：
  /  ：除法，结果总是浮点数（8 / 3 = 2.666...）
  // ：整除（地板除），向下取整得到商的整数部分（8 // 3 = 2）
  %  ：取模（求余数），返回整除后剩下的余数（8 % 3 = 2）
  ** ：幂运算，2 ** 7 表示 2 的 7 次方（= 128）""")''')

md("### 任务1.2　四种基本数据类型\n创建整数、浮点数、字符串、布尔值各一个，并用 `type()` 检查类型。")
code('''i = 42            # 整数
f = 3.14          # 浮点数
s = "hello"       # 字符串
b = True          # 布尔值
for name, v in [("整数", i), ("浮点数", f), ("字符串", s), ("布尔值", b)]:
    print(f"{name}：值={v!r:8} type={type(v).__name__}")''')

md("### 任务1.3　类型转换\n执行 `int(\"123\")`、`float(\"3.14\")`、`int(3.9)`，并捕获 `int(\"goat\")` 的异常。")
code('''print("int('123')  =", int("123"), "  # 数字字符串 -> 整数")
print("float('3.14') =", float("3.14"), "  # 数字字符串 -> 浮点数")
print("int(3.9)    =", int(3.9), "  # 浮点数 -> 整数，直接截断小数部分（不是四舍五入）")

print("\\n捕获 int('goat') 的异常：")
try:
    int("goat")
except ValueError as e:
    print(f"抛出 ValueError：{e}")
    print("原因：'goat' 不含可解析的数字，无法转换为整数。")''')

md("### 任务1.4　字符串常用处理\n对 `\" Python Data Analysis \"` 完成去空白、大小写转换、切片、单词拆分，再用 `join()` 连接。")
code('''raw = " Python Data Analysis "
print("原始字符串：", repr(raw))

stripped = raw.strip()
print("strip() 去首尾空白：", repr(stripped))

print("upper() 全大写：", stripped.upper())
print("lower() 全小写：", stripped.lower())
print("title() 每个单词首字母大写：", stripped.title())

print("切片 [0:6]：", repr(stripped[0:6]))
print("切片 [:6] ：", repr(stripped[:6]))
print("切片 [-8:]：", repr(stripped[-8:]))

words = stripped.split()
print("split() 拆成单词列表：", words)

joined = "-".join(words)
print("'-'.join(words) 用连字符连接：", joined)
print("' '.join(words) 用空格还原：", " ".join(words))''')

md("### 任务1.5　字符串拼接、重复与不可变性\n比较拼接与重复；验证字符串不能直接修改单个字符，并给出构造新字符串的方式。")
code('''a, b = "Data", "Analysis"
print("拼接 a + ' ' + b =", a + " " + b)
print("重复 a * 3 =", a * 3)

print("\\n验证字符串不可变：")
try:
    s = "cat"
    s[0] = "b"        # 试图直接修改单个字符
except TypeError as e:
    print(f"  s[0] = 'b' 抛出 TypeError：{e}")

# 构造新字符串的方式
s = "cat"
new_s = "b" + s[1:]
print("  构造新字符串：'b' + s[1:] =", new_s)
new_s2 = s.replace("c", "b")
print("  或用 s.replace('c','b') =", new_s2)''')

# ===================== 实验2 =====================
md("""---
## 实验2：函数、条件、循环与递归

### 任务2.1　分数等级函数 `score_level`
90~100 优秀；80~不足90 良好；60~不足80 及格；0~不足60 不及格；超出范围抛 `ValueError`。""")
code('''def score_level(score):
    if not (0 <= score <= 100):
        raise ValueError(f"分数必须在0~100之间，实际为：{score}")
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

for s in [95, 88, 70, 58, 60, 100]:
    print(f"{s:3d} 分 -> {score_level(s)}")

print("\\n测试越界：")
for bad in [-1, 101]:
    try:
        score_level(bad)
    except ValueError as e:
        print(f"  score_level({bad}) 抛出 ValueError：{e}")''')

md("### 任务2.2　for 与 while 求 1~100 整数和")
code('''# for 循环
total_for = 0
for x in range(1, 101):
    total_for += x

# while 循环
total_while = 0
x = 1
while x <= 100:
    total_while += x
    x += 1

print("for   循环结果：", total_for)
print("while 循环结果：", total_while)
print("两者是否相等：", total_for == total_while)
print("公式 n(n+1)/2 校验：", 100 * 101 // 2)''')

md("### 任务2.3　递归版与迭代版阶乘\n约定 0! = 1，输入非负整数，比较 n = 0、1、5、10。")
code('''def factorial_rec(n):
    if n < 0:
        raise ValueError("阶乘只接受非负整数")
    if n <= 1:          # 基线：0! = 1, 1! = 1
        return 1
    return n * factorial_rec(n - 1)

def factorial_iter(n):
    if n < 0:
        raise ValueError("阶乘只接受非负整数")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

print(f"{'n':>3} | {'递归版':>10} | {'迭代版':>10} | 是否相等")
print("-" * 48)
for n in [0, 1, 5, 10]:
    r, it = factorial_rec(n), factorial_iter(n)
    print(f"{n:>3} | {r:>10} | {it:>10} | {r == it}")''')

md("### 任务2.4　`summary(values)` 与元组解包\n接收非空数值列表，以元组返回最小值、最大值、平均值，并通过元组解包接收。")
code('''def summary(values):
    if not values:
        raise ValueError("列表不能为空")
    return (min(values), max(values), sum(values) / len(values))

low, high, avg = summary([85, 58, 92, 76, 60, 89])   # 元组解包
print("最小值：", low)
print("最大值：", high)
print("平均值：", round(avg, 2))
print("返回的是元组：", isinstance(summary([1, 2, 3]), tuple))''')

md("### 任务2.5　可变参数 `sum_all(*args)`\n返回所有参数之和，分别测试无参数、单参数、多参数。")
code('''def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total

print("无参数：", sum_all())
print("单个参数 sum_all(10)：", sum_all(10))
print("多个参数 sum_all(1,2,3,4,5)：", sum_all(1, 2, 3, 4, 5))

nums = [1, 2, 3, 4]
print("配合解包 sum_all(*[1,2,3,4])：", sum_all(*nums))''')

# ===================== 实验3 =====================
md("""---
## 实验3：列表、字典、元组与基础统计

使用模拟成绩数据（非真实学生信息）：""")
code('''names = ["Alice", "Bob", "Carol", "David", "Eva", "Frank"]
scores = [85, 58, 92, 76, 60, 89]
print("names :", names)
print("scores:", scores)''')

md("### 任务3.1　zip 构建字典并遍历\n用 `zip()` 构建姓名到成绩的字典，用 `items()` 逐项输出。")
code('''score_dict = dict(zip(names, scores))
print("字典：", score_dict)
print("\\nitems() 逐项输出：")
for name, score in score_dict.items():
    print(f"  {name:6s} : {score}")''')

md("### 任务3.2　enumerate 输出序号\n用 `enumerate()` 输出序号、姓名、成绩，序号从 1 开始。")
code('''for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"  序号{idx}: {name:6s} 成绩 {score}")''')

md("### 任务3.3　列表推导式\n提取及格学生姓名，并生成所有成绩的平方列表。")
code('''passed_names = [name for name, score in zip(names, scores) if score >= 60]
print("及格学生姓名：", passed_names)

squared = [s ** 2 for s in scores]
print("成绩平方列表：", squared)''')

md("### 任务3.4　基础统计与格式化\n计算人数、平均分、最高分、最低分、及格率；平均分保留两位小数、及格率用百分数。")
code('''count = len(scores)
avg_score = sum(scores) / count
max_score = max(scores)
min_score = min(scores)
pass_count = sum(1 for s in scores if s >= 60)
pass_rate = pass_count / count

print(f"人数：{count}")
print(f"平均分：{avg_score:.2f}")
print(f"最高分：{max_score}")
print(f"最低分：{min_score}")
print(f"及格率：{pass_rate:.1%}")
print(f"（及格率两位小数：{pass_rate * 100:.2f}%）")''')

md("### 任务3.5　别名与浅拷贝的区别\n比较 `alias = scores` 与 `copied = scores.copy()`。使用**单独的演示列表**，避免改动原始成绩。")
code('''demo = [1, 2, 3]
alias = demo            # 别名：指向同一个列表对象
copied = demo.copy()    # 浅拷贝：创建一个新列表

alias[0] = 99
print("修改 alias[0] = 99 后：")
print("  原列表 demo :", demo,  "  <- 被改动，alias 与 demo 是同一对象")
print("  别名 alias  :", alias)
print("  副本 copied :", copied, " <- 不受影响，copy() 是独立的新列表")
print("\\n身份判断：alias is demo =", alias is demo, "；copied is demo =", copied is demo)''')

md("### 任务3.6　元组不可变与不等长 zip\n用元组保存一条记录，验证元素不能重新赋值；观察长度不同的两个序列 zip 的结果。")
code('''record = ("Alice", 85, "A")
print("元组记录：", record)
print("尝试给元组元素重新赋值：")
try:
    record[1] = 90
except TypeError as e:
    print(f"  抛出 TypeError：{e}")

print("\\n不等长 zip（以短序列为准，多余元素被忽略）：")
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
print("  zip([1..5], ['a','b','c']) =", list(zip(a, b)))''')

# ===================== 实验4 =====================
md("""---
## 实验4：文件读写、异常处理与模块

### 任务4.1　查看目录、构造路径并创建数据目录
用 `os.getcwd()` 查看工作目录，`os.path.join()` 构造路径，`os.makedirs(..., exist_ok=True)` 建目录。""")
code('''print("当前工作目录 os.getcwd()：", os.getcwd())

data_dir = os.path.join(os.getcwd(), "exp01_data")
data_path = os.path.join(data_dir, "students.txt")
os.makedirs(data_dir, exist_ok=True)

print("数据目录：", data_dir)
print("students.txt 路径：", data_path)
print("目录是否存在：", os.path.isdir(data_dir))''')

md("### 任务4.2　写入并读取 students.txt\n用 `with open(..., encoding='utf-8')` 写入数据，再读取、跳过表头、用字符串方法解析。")
code('''content = """name,score
Alice,85
Bob,58
Carol,92
David,76
Eva,60
Frank,89
Grace,abc
Henry,105
Incomplete
"""

# 写入（w 模式）
with open(data_path, "w", encoding="utf-8") as f:
    f.write(content)

# 读取并跳过表头
with open(data_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip()
print("表头：", header)
print("\\n用字符串方法解析每行（split(',')）：")
for line in lines[1:]:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    print(f"  原始={line:12s} 拆分={parts}")''')

md("### 任务4.3　`parse_student(line)` 函数\n成绩转整数，检查字段数量、姓名是否为空、成绩范围；无效抛 `ValueError`。")
code('''def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误，期望2个，实际{len(fields)}个：{line!r}")
    name, score_text = fields[0].strip(), fields[1].strip()
    if name == "":
        raise ValueError(f"姓名为空：{line!r}")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是合法整数：{score_text!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出0~100范围：{score}")
    return {"name": name, "score": score}

print("有效示例 parse_student('Alice,85') =", parse_student("Alice,85"))''')

md("### 任务4.4　按行处理并记录错误\n捕获无效记录异常，记录行号与原因，继续处理后续行；有效记录保存为字典列表。")
code('''valid_records = []
errors = []

# 从文件第2行（数据行）开始，enumerate 从 2 开始计数行号
for line_no, line in enumerate(lines[1:], start=2):
    line = line.strip()
    if not line:
        continue
    try:
        rec = parse_student(line)
    except ValueError as e:
        errors.append((line_no, line, str(e)))
        print(f"[第{line_no}行] 无效：{line:10s} 原因：{e}")
    else:
        valid_records.append(rec)

print(f"\\n有效记录（{len(valid_records)}条）：")
for r in valid_records:
    print("  ", r)''')

md("### 任务4.5　写 report.txt：演示 w 与 a 模式\n将有效数、无效数、平均分、及格率写入 report.txt，并演示 `w`（覆盖）与 `a`（追加）。")
code('''v_scores = [r["score"] for r in valid_records]
v_count = len(valid_records)
e_count = len(errors)
v_avg = sum(v_scores) / v_count
v_pass_rate = sum(1 for s in v_scores if s >= 60) / v_count

report_path = os.path.join(data_dir, "report.txt")

# --- w 模式：写入，会覆盖（清空）已有内容 ---
base_report = (
    "学生成绩统计报告\\n"
    f"有效记录数: {v_count}\\n"
    f"无效记录数: {e_count}\\n"
    f"平均分: {v_avg:.2f}\\n"
    f"及格率: {v_pass_rate:.2%}\\n"
)
with open(report_path, "w", encoding="utf-8") as f:
    f.write(base_report)
print("已用 w 模式写入基础报告。")

# --- a 模式：追加，不覆盖已有内容 ---
with open(report_path, "a", encoding="utf-8") as f:
    f.write("----- 以下由 a 模式追加，不会覆盖原有内容 -----\\n")
    f.write("说明：w 模式会清空并重建文件，a 模式只在文件末尾追加。\\n")
print("已用 a 模式追加附注。")

print("\\n===== report.txt 最终内容 =====")
with open(report_path, "r", encoding="utf-8") as f:
    print(f.read())''')

md("### 任务4.6　pickle 序列化与恢复\n用 `pickle.dump()` 保存有效记录，`pickle.load()` 读取并验证相等。")
code('''import pickle

pkl_path = os.path.join(data_dir, "students.pkl")
with open(pkl_path, "wb") as f:
    pickle.dump(valid_records, f)

with open(pkl_path, "rb") as f:
    restored = pickle.load(f)

print("恢复的数据：", restored)
print("与原数据是否相等：", restored == valid_records)''')

md("### 任务4.7　调用自建模块 student_utils\n`parse_student()` 已保存到 Notebook 同级的 `student_utils.py`，通过 `import` 调用。")
code('''import student_utils
from student_utils import parse_student as module_parse

print("模块文件：", student_utils.__file__)
print("有效输入 module_parse('Grace,100') ->", module_parse("Grace,100"))
print("无效输入 module_parse('Grace,abc') 测试：")
try:
    module_parse("Grace,abc")
except ValueError as e:
    print(f"  抛出 ValueError：{e}")''')

md("### 任务4.8　捕获 FileNotFoundError\n读取一个明确不存在的文件，捕获 `FileNotFoundError` 并输出说明。")
code('''missing = os.path.join(data_dir, "definitely_not_exist.txt")
try:
    with open(missing, "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as e:
    print(f"捕获 FileNotFoundError：{e}")
    print("说明：该文件不存在；打开前可用 os.path.exists() 先判断。")''')

# ===================== 实验5 =====================
md("""---
## 实验5：类、继承与对象复制

### 任务5.1　定义 Student 类
在 `__init__` 中初始化 name、score，实现 `is_passed()` 和 `__str__()`。""")
code('''class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def __str__(self):
        return f"Student(name={self.name}, score={self.score})"''')

md("### 任务5.2　为每条有效记录创建对象\n输出对象信息和及格状态。")
code('''students = [Student(r["name"], r["score"]) for r in valid_records]
for st in students:
    status = "及格" if st.is_passed() else "不及格"
    print(f"{st}  状态：{status}")''')

md("### 任务5.3　GraduateStudent 子类\n增加 research_topic，用 `super().__init__()` 初始化父类属性，重写 `__str__()`。")
code('''class GraduateStudent(Student):
    def __init__(self, name, score, research_topic):
        super().__init__(name, score)
        self.research_topic = research_topic

    def __str__(self):
        return (f"GraduateStudent(name={self.name}, score={self.score}, "
                f"research_topic={self.research_topic})")

g = GraduateStudent("Alice", 85, "机器学习")
print(g)
print("是否及格：", g.is_passed(), "  # 继承自父类的方法")''')

md("### 任务5.4　直接赋值 / 浅拷贝 / 深拷贝\n构造含嵌套列表的对象，分别用直接赋值、`copy.copy()`、`copy.deepcopy()`，修改内部列表后比较；每次都从新建的原始对象开始。")
code('''import copy

def make_original():
    return {"name": "Alice", "scores": [85, 90]}

# 1) 直接赋值：引用同一个对象
orig = make_original()
direct = orig
direct["scores"][0] = 0
print("直接赋值：")
print("  修改后 orig   =", orig)
print("  direct is orig =", direct is orig, "（内部列表是同一个，改一个全改）")

# 2) 浅拷贝：外层是新对象，但内部列表仍共享
orig = make_original()
shallow = copy.copy(orig)
shallow["scores"][0] = 0
print("\\n浅拷贝 copy.copy()：")
print("  修改后 orig    =", orig)
print("  shallow is orig =", shallow is orig, "（外层不同）")
print("  内部列表共享 =", shallow["scores"] is orig["scores"], "（内部列表被一起改动）")

# 3) 深拷贝：内外层都独立
orig = make_original()
deep = copy.deepcopy(orig)
deep["scores"][0] = 0
print("\\n深拷贝 copy.deepcopy()：")
print("  修改后 orig  =", orig, "  <- 完全不受影响")
print("  deep        =", deep)
print("  内部列表独立 =", deep["scores"] is not orig["scores"])''')

# ===================== 结尾 =====================
md("""---
## 三、实验小结

| 实验 | 主要知识点 |
|---|---|
| 实验1 | 算术运算符、基本类型、类型转换、字符串常用方法与不可变性 |
| 实验2 | 函数定义、分支判断、for/while 循环、递归、元组与可变参数 |
| 实验3 | 列表/字典/元组、zip/enumerate、列表推导式、基础统计、别名与拷贝 |
| 实验4 | 文件读写、异常处理、w/a 模式、pickle、自建模块、FileNotFoundError |
| 实验5 | 类与继承、super()、浅拷贝与深拷贝的区别 |

全部代码已按顺序运行通过，无报错。""")

nb = new_notebook(cells=cells)
nb.metadata.update({
    "kernelspec": {"display_name": "Python 3 (pyda)", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11.17"},
})
out = r"C:\Users\33721\Doubao\chats\2026-10-13\new-chat\python-assignments-20244081108\exp01\20244081108_王亨泰_exp01.ipynb"
with open(out, "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("EXP01 notebook 已生成：", out, "共", len(cells), "个单元格")
