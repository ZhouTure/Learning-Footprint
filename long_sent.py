from openai import OpenAI
client = OpenAI(api_key = '',
                base_url=''
                )

# 初始化对话历史

conversation_history = [
    {"role":"system", "content": "你是一个专业、友好的AI助手。"}
    ]

while True:
    question = input('\n你:')

    if question.lower() in ['退出', 'exit', 'quit', 'q']:
        print("感谢使用，再见!")
        break

    # 添加问题到历史
    conversation_history.append({"role": "user", "content": question})

    # 请求
    print("R1:", end = "")
    stream = client.chat.completions.create(
        model = 'deepseek-r1-250528',
        messages = conversation_history,
        extra_body = {"reasoning": True},
        stream = True
    )

    # 收集响应
    assistant_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end = "", flush = True)
            assistant_response += content
    
    # 添加回复到历史
    conversation_history.append({"role": "assistant", "content": assistant_response})

    print()

