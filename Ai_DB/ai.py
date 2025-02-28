from openai import OpenAI
import os

def get_response(msg):
    client = OpenAI(
        api_key=os.getenv("skXXXXXXXXXXXXXXXXXXXXX"), # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': msg}]
        )
    print("AI回答：",completion.model_dump_json())
    return completion.model_dump_json()

# if __name__ == '__main__':
#     get_response(msg=input("Please input your message: "))
