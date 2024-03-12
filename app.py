# !pip install openai
import datetime,os
from openai import OpenAI
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")

## 填写自己的AKSK到下面空间
os.environ["OPENAI_API_KEY"] = "sk-"
preQuestion = """
根据下面推特主贴，设计一个comment，符合条件：
1. 让读者在当前情境下有共鸣的内容.
2. 让读者凭直觉System1思维方式就想点赞、转发、讨论的内容.
3. 让读者有获得感的内容.
4. 简单，深刻，让读者易于理解.
5. 30字以内，用中文回答.
6. 适用于twitter的推荐算法.
7. 适用于twitter平台内SEO.
8. 避免说教，避免广告，充满同理心，以朋友的口吻回复.
9. 要顺着主贴的话说，不要让人感觉太突兀,紧接着提出一个简单接地气容易回答的问题
10. do not use emoji

------
{xxxx}
"""
newdata = """
 >>>在这里输入贴主的话<<<
 """
def realtimeQuestion(question,day):
    print("=====")
    print("question:{}".format(question))
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    temperature=0,
    messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Answer as concisely as"
                    f" possible. Knowledge cutoff: {day}."
                ),
            },
            {"role": "user", "content": "What's today's date?"},
            {
                "role": "assistant",
                "content": f"Today is {day} in Pacific Standard Time.",
            },
            {"role": "user", "content": question},
        ],
    )
    return(response.choices[0].message.content)
print(realtimeQuestion(preQuestion.replace("{xxxx}",newdata),formatted_date))

