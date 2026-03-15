# 带调试信息的聊天机器人代码
from openai import OpenAI
import tkinter as tk
from tkinter import scrolledtext, messagebox
import traceback

print("✅ 代码启动")

# 填入你的 API Key
API_KEY = "sk-dcc503fd4f714871b37bda8a07ea2031"

print("📦 正在初始化 OpenAI 客户端...")
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

def send_message():
    user_text = entry.get("1.0", tk.END).strip()
    if not user_text:
        return
    
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "你：" + user_text + "\n")
    entry.delete("1.0", tk.END)

    try:
        print("📤 正在发送请求...")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response.choices[0].message.content
        print("🎉 请求成功！")
        chat_box.insert(tk.END, "机器人：" + reply + "\n\n")
    except Exception as e:
        print("❌ 请求失败！")
        traceback.print_exc()  # 打印完整错误
        messagebox.showerror("错误", f"失败原因：{str(e)}")
    
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

print("🖥️ 正在创建图形界面...")
root = tk.Tk()
root.title("AI 聊天机器人（调试版）")
root.geometry("600x500")

chat_box = scrolledtext.ScrolledText(root, width=70, height=20)
chat_box.pack(pady=10)
chat_box.config(state=tk.DISABLED)

entry = tk.Text(root, width=50, height=3)
entry.pack(pady=5)

send_btn = tk.Button(root, text="发送", command=send_message)
send_btn.pack()

print("🚀 启动界面循环...")
root.mainloop()