import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "乐融"
        self.website = "https://www.letv.com/"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        乐融是融创文化集团成员企业，是一家以互联网智能设备制造、软件开发、内容娱乐服务为一体的高科技综合型企业。
        '''

        self.cellphoneUrl = "http://sso.letv.com/user/checkMobileExists/mobile/"
        self.emailUrl = "http://sso.letv.com/user/checkEmailExists/email/"
        self.usernameUrl = ""

    def verifyCellphone(self):
        url = self.cellphoneUrl+self.content
        resp = requests.get(url)
        if "\"result\":false" in resp.text:
            return True
        else:
            return False

    def verifyEmail(self):
        url = self.emailUrl + self.content
        resp = requests.get(url)
        if "\"result\":false" in resp.text:
            return True
        else:
            return False

    def verifyUsername(self):
        return False
