import requests, re, warnings
import json

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "百度"
        self.website = "https://www.baidu.com/"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        百度（Nasdaq：BIDU）是中国最大的中文搜索引擎、最大的中文网站。
        '''

        self.cellphoneUrl = "https://passport.baidu.com/v2/?regphonecheck&phone=15846007767&isexchangeable=1"
        self.emailUrl = "https://passport.baidu.com/v2/?regmailcheck"
        self.usernameUrl = "https://passport.baidu.com/v2/?regnamesugg"

    def verifyCellphone(self):
        data = {"phone": self.content, "isexchangeable": 1}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text[1:-1])
        except:
            return False
        if res["errno"] == 400005:
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"email": self.content}
        resp = requests.get(self.emailUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text[1:-1])
        except:
            return False
        if res["errno"] == 110023:
            return True
        else:
            return False

    def verifyUsername(self):
        data = {"username": self.content}
        resp = requests.get(self.usernameUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text[1:-1])
        except:
            return False
        if res["userexsit"] == 1:
            return True
        else:
            return False
