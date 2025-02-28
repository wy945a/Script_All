import os
import requests
import base64
import json

class AIModel:
    def __init__(self):
        self.api_key = os.getenv("ALIYUN_API_KEY") or "sk-xxxxxxxxxxx"
        self.access_key_id = os.getenv("ALIYUN_ACCESS_KEY_ID") or "your_access_key_id_here"

    def _send_request(self, data):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        try:
            response = requests.post(
                "https://dashscope.aliyuncs.com/api/v1/dashscope/conversation",
                headers=headers,
                json=data,
                verify=True  # 设置为False以忽略SSL证书验证（仅用于调试）
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return None
        except requests.exceptions.SSLError as e:
            print(f"SSL Error occurred: {e}")
            return None

    def predict_element(self, screenshot_path, description):
        """根据截图和描述预测页面元素"""
        with open(screenshot_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "model": "qwen-turbo",
            "messages": [
                {'role': 'system', 'content': 'You are an assistant that can identify UI elements based on screenshots and descriptions.'},
                {'role': 'user', 'content': f"Given this screenshot and the description '{description}', find the corresponding UI element."}
            ],
            "image": encoded_image
        }
        result = self._send_request(data)
        return result['choices'][0]['message']['content'] if result else None

    def predict_user_action(self, context):
        """根据上下文预测用户行为"""
        data = {
            "model": 'qwen-turbo',
            "messages": [
                {'role': 'system', 'content': 'You are an assistant that can predict user actions based on context.'},
                {'role': 'user', 'content': f"Given the following context: {context}, what should the user do next?"}
            ]
        }
        result = self._send_request(data)
        return result['choices'][0]['message']['content'] if result else None