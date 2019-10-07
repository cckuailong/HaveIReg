import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/07"
        self.name = "暴风影音"
        self.website = "http://www.baofeng.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        暴风影音是北京暴风科技有限公司推出的一款视频播放器，该播放器兼容大多数的视频和音频格式。
        '''

        self.cellphoneUrl = "https://sso.baofeng.com/new/api/is_mobile_used"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"appid": 8637, "sign": "32a4a7b48d4a1a12f445ac51e878cf2e5d9aa3c5", "mobile": self.content}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["is_used"] == 1:
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
