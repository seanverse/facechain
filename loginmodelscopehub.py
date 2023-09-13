from modelscope.hub.api import HubApi

#通过给login()函数给其他.py文件调用，函数内调用HubAPI传入 ACCESS_TOKEN进行login; login成功则返回True,login失败返会False
def hublogin():
    YOUR_ACCESS_TOKEN = '48345cd8-efb2-4724-8cd2-a4b96fb4239b'
    api = HubApi()
    if api.login(YOUR_ACCESS_TOKEN):
        return True
    else:
        return False


