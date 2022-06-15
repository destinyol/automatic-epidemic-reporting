from windows本地.mainwork import mainWork
from windows本地.localLog import saveLogAsTXT
import email_alert

if __name__ == "__main__":
    nameDict = mainWork()
    email_alert.if_send(nameDict)
