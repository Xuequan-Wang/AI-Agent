from agent.code_analyzer import CodeAnalyzer
from agent.templates import build_report_template
from agent.llm_helper import generate_with_llm


class ReportAgent:
    def __init__(self, use_llm=True):
        self.analyzer = CodeAnalyzer()
        self.use_llm = use_llm

    def generate_report(self, topic, requirement, raw_content):
        analysis = self.analyzer.analyze(raw_content)

        if self.use_llm:
            prompt = f"""
实验主题：{topic}
实验要求：{requirement}
实验内容：{raw_content}

请生成一份完整、规范的实验报告，包括：
实验目的、实验原理、实验步骤、代码分析、实验结果、实验总结。
"""
            return generate_with_llm(prompt)

        return build_report_template(topic, requirement, analysis, raw_content)
