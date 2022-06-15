from mainwork import mainWork
from localLog import saveLogAsTXT
import email_alert

if __name__ == "__main__":
    res = mainWork()
    saveLogAsTXT(res)
    email_alert.if_send(res)
