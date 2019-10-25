import requests, re, warnings
import json

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "哔哩哔哩"
        self.website = "https://www.bilibili.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        bilibili是一家弹幕站点,大家可以在这里找到许多的欢乐。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = ""
        self.usernameUrl = "https://passport.bilibili.com/web/generic/check/nickname"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"nickName": self.content}
        resp = requests.get(self.usernameUrl, params=data, verify=False, timeout=3)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == 2001:
            return True
        else:
            return False
