# AI-Agent：智能实验报告助手

本项目是一个面向高校课程实验、工程实训和学习辅助场景的智能实验报告生成 AI Agent。

它可以根据用户输入的实验主题、实验要求、代码片段或实验结果，自动生成结构完整、语言规范的实验报告，帮助学生提高实验报告和课程设计文档的撰写效率。

## 功能特点

- 自动理解实验主题和报告要求
- 支持分析代码片段中的函数、头文件和关键语句
- 自动生成实验报告标准结构
- 支持生成实验目的、实验原理、实验步骤、程序分析、结果分析和实验总结
- 支持将生成结果保存为 Markdown 文件
- 适用于嵌入式、自动控制、Python 编程、数据分析等课程实验

## 项目结构

```text
AI-Agent/
├── main.py
├── agent/
│   ├── __init__.py
│   ├── report_agent.py
│   ├── code_analyzer.py
│   └── templates.py
├── examples/
│   └── stm32_temperature_example.txt
├── outputs/
│   └── .gitkeep
├── requirements.txt
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行项目

```bash
python main.py
```

### 3. 示例输入

```text
请输入实验主题：STM32 温度采集实验
请输入实验要求：使用 ADC 采集温度数据，并通过串口输出
请输入代码、实验说明或运行结果。输入 END 结束：
#include "stm32f10x.h"
#include "adc.h"
#include "usart.h"

int main(void)
{
    uart_init(115200);
    ADC_Init();

    while(1)
    {
        int value = Get_Adc_Average(0, 10);
        printf("value = %d\r\n", value);
    }
}
END
```

### 4. 输出结果

程序会在 `outputs/` 文件夹中生成一份 Markdown 格式的实验报告：

```text
outputs/experiment_report.md
```

## 应用场景

- 嵌入式系统实验报告
- STM32/单片机课程设计
- 自动控制实验报告
- Python 程序设计实验报告
- 数据分析实验报告
- 毕业设计阶段性总结

## 项目总结

本项目通过 AI Agent 的思想，将实验报告撰写过程拆分为任务理解、内容分析、报告生成和结果保存四个步骤，实现了一个简单但完整的智能报告助手原型。
