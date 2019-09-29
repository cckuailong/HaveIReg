import requests, re, warnings
import json
warnings.filterwarnings("ignore")
headers = {
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://www.iqiyi.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.iqiyi.com/iframe/loginreg?ver=1&is_reg=1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "爱奇艺"
        self.website = "https://www.iqiyi.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        百度旗下的一家专注于提供免费、高清网络视频服务的大型视频网站。
        '''

        self.cellphoneUrl = "https://passport.iqiyi.com/apis/user/check_account.action"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"account":self.content, "agenttype":1}
        resp = requests.post(self.cellphoneUrl, headers=headers, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["data"] == False:
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
