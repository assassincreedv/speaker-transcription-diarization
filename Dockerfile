FROM python:3.13-slim

# 2. 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    cmake \
    pkg-config \
    git \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# 4. 创建工作目录
WORKDIR /app

# 5. 拷贝项目文件
COPY . /app

# 6. 安装 Python 依赖
RUN pip install -r requirements.txt

# 7. 暴露端口
EXPOSE 8000

# 8. 启动命令（自动运行 Flask）
CMD ["python", "app.py"]