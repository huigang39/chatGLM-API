# 使用官方的 Python 基础镜像
FROM python:3.9-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到工作目录中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV ACCESS_KEY your_access_key
ENV SECRET_KEY your_secret_key

# 暴露端口
EXPOSE 2333

# 运行应用
CMD ["python", "apiRequest.py"]
CMD ["sleep", "5"]
CMD ["python", "test.py"]