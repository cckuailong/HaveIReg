import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "4399"
        self.website = "http://www.4399.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        4399是中国最大的小游戏专业网站,免费为你提供小游戏大全。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = ""
        self.usernameUrl = "http://ptlogin.4399.com/ptlogin/isExist.do"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"username": self.content, "appId": "www_home", "regMode": "reg_normal", "v": 3}
        resp = requests.get(self.usernameUrl, params=data, verify=False)
        if resp.text == "0":
            return False
        else:
            return True
