import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "果壳网"
        self.website = "https://www.guokr.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        果壳网是一个泛科技主题网站,提供负责任、有智趣、贴近生活的内容,你可以在这里阅读、分享、交流、提问。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = "https://account.guokr.com/apis/auth/email.json?retrieve_type=is_available&email={}"
        self.usernameUrl = ""

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        data = {"email": self.content}
        resp = requests.get(self.emailUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if "error_code" in res and res["error_code"] == 200101:
            return False
        if res["ok"] == True:
            return False
        else:
            return True

    def verifyUsername(self):
        return False
