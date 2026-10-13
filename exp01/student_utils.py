# -*- coding: utf-8 -*-
"""
student_utils.py
实验01 实验4：将解析学生记录的函数封装为可复用模块。

parse_student(line) 负责解析一行 "name,score" 格式的文本：
- 字段数量必须恰好为 2；
- 姓名不能为空；
- 成绩必须能转换为整数，且在 0~100（含）范围内；
任何不满足条件的情况都抛出 ValueError，并附带明确原因。
"""


def parse_student(line):
    """解析一行学生记录。

    参数
    ----
    line : str
        形如 "Alice,85" 的单行文本，字段用英文逗号分隔。

    返回
    ----
    dict
        {"name": 姓名字符串, "score": 成绩整数}

    异常
    ----
    ValueError
        字段数量不对、姓名为空、成绩不是整数或超出 0~100 时抛出。
    """
    # 去除首尾空白（含换行符），再按英文逗号切分
    fields = line.strip().split(",")

    # 1) 检查字段数量：必须恰好是 2 个字段（name, score）
    if len(fields) != 2:
        raise ValueError(f"字段数量错误，期望2个，实际{len(fields)}个：{line!r}")

    name, score_text = fields[0].strip(), fields[1].strip()

    # 2) 检查姓名是否为空
    if name == "":
        raise ValueError(f"姓名为空：{line!r}")

    # 3) 成绩必须能转换为整数（非法文本如 abc 会触发 ValueError）
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是合法整数：{score_text!r}")

    # 4) 成绩必须在 0~100 范围内
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出0~100范围：{score}")

    return {"name": name, "score": score}
