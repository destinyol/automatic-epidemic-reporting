import json
import time


def saveLogAsTXT(dictData):
    with open("option.json", 'r', encoding='utf-8') as fw:
        option = json.load(fw)
    if option["localLog"] == "open":
        nowTime = time.strftime("%Y-%m-%d", time.localtime())
        step = str(dictData)
        if '失败' in dictData.values():
            with open("log/" + nowTime + "(有失败记录).json", 'w', encoding='utf-8') as fw:
                json.dump(dictData, fw, indent=4, ensure_ascii=False)
        else:
            with open("log/" + nowTime + "(成功).json", 'w', encoding='utf-8') as fw:
                json.dump(dictData, fw, indent=4, ensure_ascii=False)