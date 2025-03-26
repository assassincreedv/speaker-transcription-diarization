from funasr import AutoModel

model = AutoModel(
    model="speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    vad_model="speech_fsmn_vad_zh-cn-16k-common-pytorch",
    punc_model="punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
    spk_model="speech_campplus_sv_zh-cn_16k-common",
    device="cuda:0",
    batch_size=5
)

if __name__ == '__main__':
    res = model.generate(
        input=f"/Users/xiaosonghu/Repo/FunASR/examples/industrial_data_pretraining/sense_voice/audio.wav",
        language="auto",

    )
    for sentence in res[0].get('sentence_info'):
        print('text:' + str(sentence.__getitem__('text')) + " " + 'speaker: ' + str(sentence.__getitem__('spk')) + ' startTime: ' + str(sentence.__getitem__('start')))
