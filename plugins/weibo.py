import requests, re, warnings
import json
warnings.filterwarnings("ignore")
headers = {
            "Host": "weibo.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://weibo.com/signup/signup.php",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/07"
        self.name = "微博"
        self.website = "https://weibo.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        微博（Weibo）是一种基于用户关系信息分享、传播以及获取的通过关注机制分享简短实时信息的广播式的社交媒体
        '''

        self.cellphoneUrl = "https://weibo.com/signup/v5/formcheck"
        self.emailUrl = "https://weibo.com/signup/v5/formcheck"
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"type": "mobilesea", "zone": "0086","value": self.content}
        resp = requests.get(self.cellphoneUrl, headers=headers, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == "600001":
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"type": "email", "value": self.content}
        resp = requests.get(self.emailUrl, headers=headers, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == "600001":
            return True
        else:
            return False

    def verifyUsername(self):
        return False
