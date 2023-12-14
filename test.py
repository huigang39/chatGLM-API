import requests

# 设置API的URL
url = 'http://localhost:2333/chat'  # 将localhost:2333替换为实际的API地址

# 设置请求数据
data = {
    'input': 'Rust会取代C/C++吗?'  # 用户输入的文字内容
}

# 发送POST请求
response = requests.post(url, json=data)

# 解析响应数据
if response.status_code == 200:
    result = response.json()
    reply = result['reply']
    print(reply)
else:
    print('请求失败:', response.text)
