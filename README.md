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

ACCESS_KEY 和 SECRET_KEY 需要去[火山引擎](https://www.volcengine.com/)官方注册账号获取。

```bash
export ACCESS_KEY=your_access_key
export SECRET_KEY=your_secret_key
```

然后，运行应用：

```bash
python apiRequest.py
```

你的应用现在应该可以在 `http://localhost:5000` 访问了。

## Docker 部署

你也可以使用 Docker 来运行这个应用。首先，构建 Docker 镜像：

```bash
docker build -t your_image_name .
```

然后，运行 Docker 容器：

```bash
docker run -p 2333:2333 -e ACCESS_KEY=your_access_key -e SECRET_KEY=your_secret_key your_image_name
```

你的应用现在应该可以在 `http://localhost:5000` 访问了。

## 贡献

欢迎提交 pull requests 来改进这个项目。

## 许可证

这个项目使用 MIT 许可证 - 查看 [LICENSE.md](LICENSE.md) 文件了解更多详情。
