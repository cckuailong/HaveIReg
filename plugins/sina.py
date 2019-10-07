import requests, re, warnings
import json
warnings.filterwarnings("ignore")
headers = {
            "Host": "login.sina.com.cn",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://login.sina.com.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://login.sina.com.cn/signup/signup?entry=homepage",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "新浪"
        self.website = "https://www.sina.com.cn/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        新浪（NASDAQ：SINA）新浪公司是一家服务于中国及全球华人社群的网络媒体公司。
        '''

        self.cellphoneUrl = "https://login.sina.com.cn/signup/check_user.php"
        self.emailUrl = "https://login.sina.com.cn/signup/check_user.php"
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"name": self.content, "format": "json", "from": "mobile"}
        resp = requests.post(self.cellphoneUrl, headers=headers, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["retcode"] == 100001:
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"name": self.content, "format": "json", "from": "othermail"}
        resp = requests.post(self.emailUrl, headers=headers, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["retcode"] == 100001:
            return True
        else:
            return False

    def verifyUsername(self):
        return False
