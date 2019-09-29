import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "凯撒旅游网"
        self.website = "http://www.caissa.com.cn/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        凯撒旅游网提供专业旅游咨询；轻松实现在线预订、网上支付、订单查询功能；
        '''

        self.cellphoneUrl = "http://my.caissa.com.cn/Registered/CheckPhone"
        self.emailUrl = "http://ws.caissa.com.cn/user.ashx"
        self.usernameUrl = "http://ws.caissa.com.cn/user.ashx"

    def verifyCellphone(self):
        data = {
            "hdurl": "http://caissa.com.cn/",
            "phone": self.content
        }
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        if resp.text == "1":
            return False
        else:
            return True

    def verifyEmail(self):
        data = {"JudgeEmail": self.content}
        resp = requests.get(self.emailUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text[1:-1])
        except:
            return False
        if res["count"] == 0:
            return False
        else:
            return True

    def verifyUsername(self):
        data = {"JudgeUserName": self.content}
        resp = requests.get(self.usernameUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text[1:-1])
        except:
            return False
        if res["count"] == 0:
            return False
        else:
            return True
