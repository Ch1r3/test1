import os

from zhipuai import ZhipuAI
from IPython.display import display, Markdown, HTML

client = ZhipuAI(
  api_key=os.environ["ZHIPUAI_API_KEY"]
 )

def gen_glm_params(prompt):
    messages = [{"role": "user", "content": prompt}]
    return messages

def get_completion(prompt, model="glm-4", temperature=0.95):
    messages = gen_glm_params(prompt)
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature
    )
    if len(response.choices) > 0:
        return response.choices[0].message.content
    return "generate answer error"

def check_sensitive_words(review):
    prompt_sensitive = f"""
    你的任务是：根据通用敏感词库，帮我检测三个双引号中内容中是否含有敏感词。\
    如果没有敏感词，直接输出"无敏感词"。\
    如果有敏感词的话，指出所有的敏感词，和每个敏感词的敏感类型。

    不需要说其他无关的提示信息。

    Review text:'''{review}'''
    """
    return get_completion(prompt_sensitive)

review1 = """
我靠，你真是个混蛋，我要打死你。
"""
review2 = """
你真是个好人，我要感谢你。
"""
review3 = """
这个地方真繁华，我们一把火烧了吧。
"""

result = check_sensitive_words(review1)
print(result)

