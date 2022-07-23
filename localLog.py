import json
import os
import time


def saveLogAsTXT(dictData):
    path = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(path + "option.json", 'r', encoding='utf-8') as fw:
        option = json.load(fw)
    if option["localLog"] == "open":
        nowTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        step = str(dictData)
        if '失败' in dictData.values():
            with open(path + "log/" + nowTime + "(有失败记录).json", 'w', encoding='utf-8') as fw:
                json.dump(dictData, fw, indent=4, ensure_ascii=False)
        else:
            with open(path + "log/" + nowTime + "(成功).json", 'w', encoding='utf-8') as fw:
                json.dump(dictData, fw, indent=4, ensure_ascii=False)
