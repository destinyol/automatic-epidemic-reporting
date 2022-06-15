from mainwork import mainWork
from localLog import saveLogAsTXT

if __name__ == "__main__":
    res = mainWork()
    saveLogAsTXT(res)
    email_alert(res)
