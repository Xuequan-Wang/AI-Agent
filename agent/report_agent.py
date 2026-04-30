from agent.code_analyzer import CodeAnalyzer
from agent.templates import build_report_template


class ReportAgent:
    def __init__(self):
        self.analyzer = CodeAnalyzer()

    def generate_report(self, topic, requirement, raw_content):
        analysis = self.analyzer.analyze(raw_content)
        return build_report_template(topic, requirement, analysis, raw_content)
