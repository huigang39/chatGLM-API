# chatGLM-API

这是一个使用 Flask 和 VolcEngine MaaS API 的 chatGLM 聊天接口。

## 安装

首先，克隆这个仓库到你的本地机器：

```bash
git clone https://github.com/huigang39/chatGLM-API.git
```

然后，进入项目目录并安装依赖：

```bash
cd chatGLM-API
pip install -r requirements.txt
```

## 使用

首先，设置你的环境变量：

```bash
export ACCESS_KEY=your_access_key
export SECRET_KEY=your_secret_key
```

ACCESS_KEY 和 SECRET_KEY 需要去[火山引擎](https://www.volcengine.com/)官方注册账号获取

然后，运行应用：

```bash
python apiRequest.py
```

然后运行：

```bash
python test.py
```

可以看到终端返回了内容。

## Docker 部署

你也可以使用 Docker 来运行这个应用。首先，构建 Docker 镜像：

```bash
docker build -t your_image_name .
```

如果你不想自己构建 Docker 镜像，那么你也可以直接 pull 我构建好的镜像：

```bash
docker pull huigang39/chatglm_api
```

然后，运行 Docker 容器：

```bash
docker run -p 5000:5000 -e ACCESS_KEY=your_access_key -e SECRET_KEY=your_secret_key your_image_name
```

同样的，运行：

```bash
python test.py
```

可以看到终端返回了内容。

## 贡献

欢迎提交 pull requests 来改进这个项目。

## 许可证

这个项目使用 MIT 许可证 - 查看 [LICENSE.md](LICENSE.md) 文件了解更多详情。
