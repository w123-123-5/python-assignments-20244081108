# -*- coding: utf-8 -*-
"""构建 HW01 作业 notebook（20244081108_王亨泰_hw01.ipynb）。"""
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

cells = []
def md(src):
    cells.append(new_markdown_cell(src))
def code(src):
    cells.append(new_code_cell(src))

# ===================== 封面 =====================
md("""# 作业1：Data Types, Functions and Conditionals

- **学号**：20244081108
- **姓名**：王亨泰
- **环境**：独立 conda 虚拟环境 `pyda`（Python 3.11 + Jupyter），未使用 base 环境""")

# ===================== 第一个代码框 =====================
md("## 第一个代码框：身份与环境记录")
code('''import os, uuid, hashlib, platform, getpass

# ===== 1. 填写学号 =====
STUDENT_ID = 20244081108  # 修改为自己的学号

# ===== 2. 打印 conda 环境 =====
CONDA_ENV = os.environ.get("CONDA_DEFAULT_ENV", "base")
print(f"[Conda 环境] {CONDA_ENV}")

# ===== 3. 机器指纹（绑定当前电脑）====
MACHINE_FP = hashlib.sha256(
    f"{platform.node()}|{platform.machine()}|{platform.system()}|{uuid.getnode()}".encode()
).hexdigest()[:16]

# ===== 4. 生成唯一 ID =====
RUN_ID = f"{STUDENT_ID}-{MACHINE_FP}"
print(f"[学号] {STUDENT_ID}")
print(f"[机器指纹] {MACHINE_FP}")
print(f"[RUN_ID] {RUN_ID}")''')

# ===================== 热身 =====================
md("""---
## 热身：定义简单函数

1. `say_hi`：无参数，调用时打印 `"Hello, world!"`；
2. `goatPad`：接受一个字符串，打印该字符串并在前后加上 `"goat"`；
3. `print_n`：接受字符串 `s` 和整数 `n`，将字符串打印 `n` 次，每次单独一行。""")
code('''# 1)
def say_hi():
    print("Hello, world!")

# 2)
def goatPad(s):
    print("goat" + s + "goat")

# 3)
def print_n(s, n):
    for _ in range(n):
        print(s)

# ---- 测试 ----
print("say_hi():")
say_hi()

print("\\ngoatPad('Pad'):")
goatPad("Pad")

print("\\nprint_n('abc', 3):")
print_n("abc", 3)''')

# ===================== 欧几里得 =====================
md("""---
## 欧几里得算法

两个数 m、n 的最大公约数（GCD）是同时能整除二者的最大数。

### 1) 实现 `gcd`
假设两个输入都是整数，无需错误检查。这里采用「辗转相除法」：
不断用 `(m, n)` 替换为 `(n, m % n)`，直到余数为 0。""")
code('''def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m''')

md("### 2) 评估三组数字对的 GCD")
code('''pairs = [(2018, 2019), (1200, 300), (5040, 60)]
for m, n in pairs:
    print(f"gcd({m}, {n}) = {gcd(m, n)}")''')

md("### 3) 负数参数的行为")
code('''print("gcd(-2018, 2019) =", gcd(-2018, 2019))   # 一正一负
print("gcd(2018, -2019) =", gcd(2018, -2019))   # 一正一负
print("gcd(-1200, -300) =", gcd(-1200, -300))   # 两个都负
print("gcd(-5040, 60)  =", gcd(-5040, 60))

print("""
行为分析：
- 恰好一个参数为负时，结果仍为正数（绝对值正确）；
- 两个参数都为负时，结果为负数（如 gcd(-1200,-300) = -300）。
这种行为“部分有意义”：绝对值是正确的 GCD，但数学上 GCD 定义为非负整数，
返回负数没有意义。更严谨的做法是在函数开头先取绝对值：
    m, n = abs(m), abs(n)""")''')

# ===================== 近似欧拉数 e =====================
md("""---
## 近似欧拉数 e

自然对数的底数定义为无限和

$$e = \\sum_{k=0}^{\\infty}\\frac{1}{k!} = 1 + \\frac{1}{1} + \\frac{1}{2} + \\frac{1}{6} + \\frac{1}{24} + \\cdots$$

其中 $k!$ 是阶乘，约定 $0! = 1$。

### 1) `euler_limit(n)`
用伯努利极限 $(1+\\frac{1}{x})^x$（取 $x=n$）近似 e。""")
code('''def euler_limit(n):
    return float((1 + 1 / n) ** n)

for n in [1, 10, 100, 1000, 100000]:
    print(f"euler_limit({n:>6}) = {euler_limit(n):.10f}")''')

md("""### 2) `euler_infinite_sum(n)`
基于公式（1）的**前 n 项**之和返回 e 的近似值。

注意：函数是「1-索引」的——
- `euler_infinite_sum(0) = 0`；
- `euler_infinite_sum(1) = 1`（只含 $k=0$ 一项）；
- `euler_infinite_sum(4) = 1 + 1 + 1/2 + 1/6 \\approx 2.667$（含 $k=0,1,2,3$）。""")
code('''def euler_infinite_sum(n):
    if n == 0:
        return 0.0
    total = 0.0
    fact = 1                 # 保存 k!，递推：k! = (k-1)! * k
    for k in range(n):       # 取 k = 0..n-1，共 n 项
        if k > 0:
            fact *= k
        total += 1 / fact
    return float(total)

print("euler_infinite_sum(0) =", euler_infinite_sum(0))
print("euler_infinite_sum(1) =", euler_infinite_sum(1))
print("euler_infinite_sum(2) =", euler_infinite_sum(2))
print("euler_infinite_sum(4) =", round(euler_infinite_sum(4), 3))
print("euler_infinite_sum(10) =", round(euler_infinite_sum(10), 10))''')

md("### 3) `euler_approx(epsilon)`\n用 `while` 循环不断增加项数，直到近似值与真实值 e（`math.exp(1)`）的误差在 `epsilon` 以内。")
code('''import math

def euler_approx(epsilon):
    n = 0
    while abs(euler_infinite_sum(n) - math.exp(1)) >= epsilon:
        n += 1
    return euler_infinite_sum(n)

for eps in [0.1, 0.01, 0.001, 1e-6]:
    approx = euler_approx(eps)
    print(f"epsilon={eps:g}  近似值={approx:.10f}  实际误差={abs(approx-math.exp(1)):.2e}")''')

md("### 4) `print_euler_sum_table(n)`\n打印 `euler_infinite_sum(k)`，k 从 1 到 n，每行一个。")
code('''def print_euler_sum_table(n):
    for k in range(1, n + 1):
        print(euler_infinite_sum(k))

print_euler_sum_table(10)''')

# ===================== 测试整数属性 =====================
md("""---
## 测试整数属性

正整数 n 是 2 的幂，当且仅当 $n = 2^p$（$p \\ge 0$）。

### 1) `is_power_of_2(n)`
返回布尔值，**不使用 `math.sqrt`**，只用除法和模运算：
反复除以 2，中途若出现奇数则不是 2 的幂。""")
code('''def is_power_of_2(n):
    while n > 1:
        if n % 2 != 0:      # 还没除到1就出现奇数
            return False
        n = n // 2
    return n == 1

print("是 2 的幂：")
for n in [1, 2, 4, 8, 16, 1024]:
    print(f"  is_power_of_2({n:>4}) = {is_power_of_2(n)}")
print("不是 2 的幂：")
for n in [3, 6, 10, 100, 0]:
    print(f"  is_power_of_2({n:>4}) = {is_power_of_2(n)}")''')

md("### 2) `is_power(b, n)`\n推广为：n 是否为 b 的幂（$n = b^p$）。需额外处理 `b=1`（1 的任何幂都是 1，会死循环）。")
code('''def is_power(b, n):
    if b == 1:                 # 1^p 恒为 1，只有 n==1 成立
        return n == 1
    if n == 1:                 # b^0 = 1
        return True
    while n > 1:
        if n % b != 0:
            return False
        n = n // b
    return n == 1

print("应为 True：")
for b, n in [(2, 8), (2, 1024), (3, 27), (10, 1000), (5, 1), (1, 1)]:
    print(f"  is_power({b}, {n:>4}) = {is_power(b, n)}")
print("应为 False：")
for b, n in [(2, 6), (3, 10), (10, 500), (1, 5)]:
    print(f"  is_power({b}, {n:>4}) = {is_power(b, n)}")''')

md("""---
## 小结

- 掌握了无参/带参/可计数循环的简单函数定义；
- 用辗转相除法实现 GCD，并分析了负数输入的符号问题；
- 用极限式、级数求和、按误差阈值（while）、打印表格四种方式近似 e；
- 用除法和模运算判断 2 的幂，并推广到任意底数 b 的幂判定。""")

nb = new_notebook(cells=cells)
nb.metadata.update({
    "kernelspec": {"display_name": "Python 3 (pyda)", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11.17"},
})
out = r"C:\Users\33721\Doubao\chats\2026-10-13\new-chat\python-assignments-20244081108\hw01\20244081108_王亨泰_hw01.ipynb"
with open(out, "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("HW01 notebook 已生成：", out, "共", len(cells), "个单元格")
