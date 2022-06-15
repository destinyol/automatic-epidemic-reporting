import time


def saveLogAsTXT(dictDatax):
    dictData = {'2017404032':'成功','2017404066':'失败'}
    nowTime = time.strftime("%Y-%m-%d", time.localtime())
    step = str(dictData)
    if '失败' in dictData.values():
        file = open('log/'+nowTime+'(有失败记录).txt', 'w')
    else:
        file = open('log/' + nowTime + '(成功).txt', 'w')
    file.writelines(step)
    file.close()