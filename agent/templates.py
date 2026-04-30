def build_report_template(topic, requirement, analysis, raw_content):
    return f"""# {topic} 实验报告

## 实验目的

完成 {topic} 的实验，并掌握相关原理。

## 实验要求

{requirement}

## 实验分析

检测模块：{analysis.get('modules')}

函数：{analysis.get('functions')}

## 实验总结

本实验完成了基本功能，实现了预期目标。

## 原始内容

{raw_content}
"""
