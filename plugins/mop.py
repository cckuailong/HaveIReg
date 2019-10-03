import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/03"
        self.name = "猫扑网"
        self.website = "http://www.mop.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        猫扑网的雏形是猫扑大杂烩，是中国知名的中文网络社区之一，拥有注册用户1.3亿人。
        '''

        self.cellphoneUrl = "http://passport.mop.com/ajax/mobileWasBound?mobile=15846007767"
        self.emailUrl = ""
        self.usernameUrl = "http://passport.mop.com/register/uniqueName"

    def verifyCellphone(self):
        resp = requests.get(self.cellphoneUrl)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == 0:
            return False
        else:
            return True

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"userName": self.content}
        resp = requests.get(self.usernameUrl, params=data)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["msg"] == "用户名重复":
            return True
        else:
            return False
