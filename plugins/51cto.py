import requests, re, warnings
warnings.filterwarnings("ignore")

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/27"
        self.name = "51CTO"
        self.website = "https://www.51cto.com"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        51CTO传媒是专注于IT技术创新与发展的互联网媒体平台，由一批资深互联网专业人士创立于2005年。
        '''

        self.cellphoneUrl = "https://home.51cto.com/user/check-user"
        self.emailUrl = ""
        self.usernameUrl = "https://home.51cto.com/user/check-user"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"username": self.content, "is_ie": 0}
        resp = requests.get(self.usernameUrl, params=data)
        print(resp.text)
        if "此用户名可用" in resp.text:
            return False
        else:
            return True

testReg = TestReg("15846007767")
print(testReg.verifyCellphone())