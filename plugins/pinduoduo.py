import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "拼多多"
        self.website = "https://pinduoduo.zhiye.com"
        self.category = "EC"
        self.iconUrl = ""
        self.desc = '''
        拼多多作为新电商开创者,致力于将娱乐社交的元素融入电商运营中,通过“社交+电商”的模式,让更多的用户带着乐趣分享实惠,享受全新的共享式购物体验。
        '''

        self.cellphoneUrl = "https://pinduoduo.zhiye.com/User/Account/CheckPhoneOccupied"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"mobile": self.content, "businessType": 1}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["Message"] == "registered":
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
