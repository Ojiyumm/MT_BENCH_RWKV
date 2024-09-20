import requests
import json

# API 端点
url = "https://lmzh.top/v1/chat/completions"

# 请求头部信息
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-fodxjDC0Zl5j82E2B97583943a6b4dBfBeF509C330D68717"
}

# 请求体
data = {
    "max_tokens": 1024,
    "model": "gpt-4o",
    "temperature": 1,
    "top_p": 0.3,
    "presence_penalty": 0,
    "frequency_penalty": 1,
    "messages": [
        {"role": "user", "content": "hi"}
    ]
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查请求是否成功
if response.status_code == 200:
    # 输出响应结果
    print("Response:", response.json())
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

