# utils.py
import requests
from io import BytesIO

def download_audio(url):
    r = requests.get(url)
    r.raise_for_status()
    return BytesIO(r.content)  # 不写入磁盘

def process_audio(audio_data):
    """
    audio_data: BytesIO 或其他类似文件对象
    """
    from asr_woker import model  # 延迟引入
    res = model.generate(input=audio_data, language="auto")
    results = []
    for sentence in res[0].get("sentence_info"):
        results.append({
            "text": sentence["text"],
            "speaker": sentence["spk"],
            "start": sentence["start"]
        })
    return results

def read_uploaded_file(file_storage):
    return BytesIO(file_storage.read())
