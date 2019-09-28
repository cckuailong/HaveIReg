import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "58同城"
        self.website = "http://www.58.com"
        self.category = "EC"
        self.iconUrl = ""
        self.desc = '''
        58同城2005年12月创立于北京，为用户提供“本地、免费、真实、高效”的生活服务。
        '''

        self.cellphoneUrl = "https://passport.58.com/ajax/checknickname"
        self.emailUrl = ""
        self.usernameUrl = "https://passport.58.com/ajax/checknickname"

    def verifyCellphone(self):
        data = {"nickname": self.content, "source": "58-default-pc"}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        if resp.text == "1":
            return False
        else:
            return True

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"nickname": self.content, "source":"58-default-pc"}
        resp = requests.get(self.usernameUrl, params=data, verify=False)
        if resp.text == "1":
            return False
        else:
            return True
