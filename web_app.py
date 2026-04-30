import streamlit as st
from agent.report_agent import ReportAgent

st.set_page_config(page_title="AI实验报告助手", layout="wide")

st.title("🤖 AI 实验报告助手")

agent = ReportAgent()

with st.form("report_form"):
    topic = st.text_input("实验主题")
    requirement = st.text_area("实验要求")
    content = st.text_area("代码 / 实验说明")

    submit = st.form_submit_button("生成报告")

if submit:
    report = agent.generate_report(topic, requirement, content)
    st.success("生成成功！")
    st.markdown(report)

    st.download_button(
        label="下载报告",
        data=report,
        file_name="experiment_report.md",
        mime="text/markdown"
    )
