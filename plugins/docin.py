import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "豆丁网"
        self.website = "http://www.docin.com/"
        self.category = "EDU"
        self.iconUrl = ""
        self.desc = '''

        '''

        self.cellphoneUrl = ""
        self.emailUrl = "http://www.docin.com/vdwrutil/checkLoginEmail.do"
        self.usernameUrl = "http://www.docin.com/jsp_cn/jquery/login/reg_check.jsp?flag=name"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        data = {"loginEmail": self.content}
        resp = requests.get(self.emailUrl, params=data)
        if "true" in resp.text:
            return False
        else:
            return True

    def verifyUsername(self):
        data = {"loginName": self.content}
        resp = requests.get(self.usernameUrl, params=data)
        if "true" in resp.text:
            return False
        else:
            return True
