from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from agent.report_agent import ReportAgent


def main():
    console = Console()

    console.print(
        Panel.fit(
            "智能实验报告助手 AI Agent",
            subtitle="AI-Agent Project",
            border_style="green"
        )
    )

    topic = console.input("[bold cyan]请输入实验主题：[/bold cyan]").strip()
    requirement = console.input("[bold cyan]请输入实验要求：[/bold cyan]").strip()

    console.print("\n[bold cyan]请输入代码、实验说明或运行结果。输入 END 结束：[/bold cyan]")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    raw_content = "\n".join(lines)

    agent = ReportAgent()
    report = agent.generate_report(
        topic=topic,
        requirement=requirement,
        raw_content=raw_content
    )

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "experiment_report.md"
    output_file.write_text(report, encoding="utf-8")

    console.print("\n[bold green]实验报告已生成：[/bold green]")
    console.print(str(output_file))

    console.print("\n[bold yellow]报告预览：[/bold yellow]")
    console.print(Panel(report[:1500] + "\n\n......", border_style="yellow"))


if __name__ == "__main__":
    main()
