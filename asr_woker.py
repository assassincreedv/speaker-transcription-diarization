# asr_worker.py
from funasr import AutoModel
import json
import os
from utils import download_audio, process_audio

model = AutoModel(
    model="speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    vad_model="speech_fsmn_vad_zh-cn-16k-common-pytorch",
    punc_model="punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
    spk_model="speech_campplus_sv_zh-cn_16k-common",
    device="cuda:0",
    batch_size=5
)

def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        audio_url = message.get("link")
        print(f"[MQ] Received audio url: {audio_url}")
        audio_data = download_audio(audio_url)
        result = process_audio(audio_data)
        print("[MQ] ASR result:", result)
    except Exception as e:
        print(f"[MQ] Error: {e}")
