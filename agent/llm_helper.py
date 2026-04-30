import os
from openai import OpenAI


def generate_with_llm(prompt: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个专业的实验报告生成助手。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"LLM 调用失败，已自动切换到本地模板模式：{e}")
        return None
