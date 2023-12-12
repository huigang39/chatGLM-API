import os
from volcengine.maas import MaasService, MaasException, ChatRole
from flask import Flask, request, jsonify

app = Flask(__name__)

# 从环境变量中获取VolcEngine的Access Key和Secret Key
# ACCESS_KEY=XXXXX SECRET_KEY=YYYYY python apiRequest.py
access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')

# 创建MaasService实例
maas = MaasService('maas-api.ml-platform-cn-beijing.volces.com', 'cn-beijing')
maas.set_ak(access_key)
maas.set_sk(secret_key)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 从请求中获取用户输入的文字内容
        user_input = request.json['input']

        # 创建对话请求
        req = {
            "model": {
                "name": "chatglm-130b",
            },
            "parameters": {
                "max_new_tokens": 1000,
                "top_p": 0.92,
                "temperature": 1,
            },
            "messages": [
                {
                    "role": ChatRole.USER,
                    "content": user_input
                }
            ]
        }

        # 发送对话请求并获取回应
        resp = maas.chat(req)

        # 提取完整的回应文本
        reply = resp.choice.message.content

        # 返回回应文本给客户端
        return jsonify({'reply': reply})

    except MaasException as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()