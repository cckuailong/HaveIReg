import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "站长之家"
        self.website = "http://www.chinaz.com"
        self.category = "TOOL"
        self.iconUrl = ""
        self.desc = '''
        站长之家(中国站长站，是一家专门针对中文站点提供资讯、技术、资源、服务的网站，网站现有上百万用户。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = "http://my.chinaz.com/User/ValidateEmail"
        self.usernameUrl = "http://my.chinaz.com/User/ValidateUserName"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        data = {"email": self.content}
        resp = requests.post(self.emailUrl, data=data)
        if resp.text == "false":
            return True
        else:
            return False

    def verifyUsername(self):
        data = {"userName": self.content}
        resp = requests.post(self.usernameUrl, data=data)
        if resp.text == "false":
            return True
        else:
            return False
