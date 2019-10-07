import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/07"
        self.name = "凤凰网"
        self.website = "http://www.ifeng.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        凤凰网（凤凰新媒体，纽交所代码：FENG)是全球领先的跨平台网络新媒体公司，整合旗下综合门户凤凰网、手机凤凰网和凤凰视频三大平台。
        '''

        self.cellphoneUrl = "https://id.ifeng.com/api/checkMobile"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"u": self.content}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["message"] == "手机号不存在":
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
