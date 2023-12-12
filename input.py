import requests
import sys
import json

def send_post_request(url, input_text):
    # 设置请求数据
    data = {
        'input': input_text
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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('请输入要发送的文本作为参数')
        sys.exit(1)

    # 设置API的URL
    url = 'http://localhost:2333/chat'  # 将localhost:2333替换为实际的API地址

    # 获取命令行参数作为输入文本
    input_text = ' '.join(sys.argv[1:])

    # 发送POST请求并打印回应
    send_post_request(url, input_text)
