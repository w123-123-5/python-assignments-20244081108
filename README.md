# Python 数据分析课程作业（EXP01 & HW01）

- **学号**：20244081108
- **姓名**：王亨泰
- **运行环境**：独立 conda 虚拟环境 `pyda`（Python 3.11 + Jupyter），未使用 base 环境

## 目录结构

```
python-assignments-20244081108/
├── exp01/
│   ├── 20244081108_王亨泰_exp01.ipynb   # 实验报告01
│   ├── student_utils.py                 # 实验4 自建模块：parse_student()
│   └── exp01_data/
│       ├── students.txt                 # 原始数据（含若干无效记录）
│       ├── report.txt                   # 统计报告（w/a 模式演示）
│       └── students.pkl                 # pickle 序列化结果
├── hw01/
│   └── 20244081108_王亨泰_HW01.ipynb     # 作业1
└── build/
    ├── build_exp01.py                   # 用 nbformat 生成 EXP01 的脚本（可复现）
    └── build_hw01.py                    # 用 nbformat 生成 HW01 的脚本（可复现）
```

## 内容说明

### 实验报告01：Python 基础与数据处理入门
- **实验1**：基本运算、数据类型、类型转换、字符串常用方法与不可变性
- **实验2**：函数、条件、for/while 循环、递归、元组与可变参数
- **实验3**：列表/字典/元组、`zip`/`enumerate`、列表推导式、基础统计、别名与拷贝
- **实验4**：文件读写、异常处理、`w`/`a` 模式、pickle、自建模块、`FileNotFoundError`
- **实验5**：类与继承、`super()`、浅拷贝 `copy.copy` 与深拷贝 `copy.deepcopy`

### 作业1：Data Types, Functions and Conditionals
- 热身：`say_hi`、`goatPad`、`print_n`
- 欧几里得算法：`gcd`（含负数参数行为分析）
- 近似欧拉数 e：`euler_limit`、`euler_infinite_sum`、`euler_approx`、`print_euler_sum_table`
- 整数属性：`is_power_of_2`、`is_power`

## 如何运行

```bash
# 1. 创建并激活独立环境
conda create -n pyda python=3.11 jupyter nbconvert ipykernel -y
conda activate pyda

# 2. 在对应目录从头执行（等价于重启内核并运行全部）
cd exp01
jupyter nbconvert --to notebook --execute --inplace "20244081108_王亨泰_exp01.ipynb"

cd ../hw01
jupyter nbconvert --to notebook --execute --inplace "20244081108_王亨泰_HW01.ipynb"
```

> 两个 Notebook 均已从头执行通过，无任何报错，所有输出已填充。
