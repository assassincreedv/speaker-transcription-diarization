# app.py
from flask import Flask, request, jsonify
import os
import threading
import pika
import json
from utils import download_audio, process_audio, read_uploaded_file
from asr_woker import model, callback

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# === Flask 接口：上传本地音频文件 ===
# app.py 的 /upload 接口部分

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    audio_bytes = read_uploaded_file(file)
    result = process_audio(audio_bytes)
    return jsonify(result)


# === MQ 监听器线程 ===
def start_mq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="asr_task")
    channel.basic_consume(queue="asr_task", on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages from MQ")
    channel.start_consuming()

if __name__ == "__main__":
    # 开启 MQ 监听线程
    # mq_thread = threading.Thread(target=start_mq_consumer)
    # mq_thread.daemon = True
    # mq_thread.start()

    # 启动 Flask
    app.run(host="0.0.0.0", port=8000, debug=True)
