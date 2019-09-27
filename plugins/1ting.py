import requests, re, warnings
warnings.filterwarnings("ignore")

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/27"
        self.name = "一听音乐网"
        self.website = "https://www.1ting.com"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        一听音乐网是中国最大的在线音乐网站,提供免费歌曲在线试听、下载。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = "https://my.1ting.com/register/check"
        self.usernameUrl = "https://my.1ting.com/register/check"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        data = {"user_login": self.content}
        resp = requests.get(self.emailUrl, params=data)
        if "true" in resp.text:
            return False
        else:
            return True

    def verifyUsername(self):
        data = {"user_login": self.content}
        resp = requests.get(self.usernameUrl, params=data)
        if "true" in resp.text:
            return False
        else:
            return True
