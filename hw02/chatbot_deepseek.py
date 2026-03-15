# 这是作业专用版，直接填 API Key 就能跑
from openai import OpenAI

# 在这里填入你复制的 API Key
YOUR_API_KEY = "sk-dcc503fd4f714871b37bda8a07ea2031"

client = OpenAI(
    api_key=YOUR_API_KEY,  # 直接用
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(user_input):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("聊天机器人已启动！输入 quit 退出")
    while True:
        msg = input("你：")
        if msg.lower() == "quit":
            break
        res = chat_with_deepseek(msg)
        print("机器人：", res, "\n")