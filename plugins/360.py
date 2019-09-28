import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "360"
        self.website = "https://www.360.cn/"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        360由周鸿祎创立于2005年9月，主营以360杀毒为代表的免费网络安全平台，同时拥有问答等独立业务。
        '''

        self.cellphoneUrl = "https://login.360.cn"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"m": "checkmobile", "mobile": self.content}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        if "\"errno\":0" in resp.text:
            return False
        else:
            return True

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
