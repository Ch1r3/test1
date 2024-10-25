import os
from zhipuai import ZhipuAI
client = ZhipuAI(
  api_key=os.environ["ZHIPUAI_API_KEY"]
 )
def get_comletion_chatbot(messages, model="glm-4", temperature=0.95):
    response = client.chat.completions.create(
    model=model,  # 填写需要调用的模型编码
    messages=messages,  # 填写对话内容
    )
    print(response.choices[0].message)

messages = [
    {"role": "system", "content": "你是一个友善的机器人。"},
    {"role": "user", "content": "你好，你能提醒我的名字吗？"}
]

response = get_comletion_chatbot(messages)
print(response)