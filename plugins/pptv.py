import requests, re, warnings
import json
warnings.filterwarnings("ignore")
headers = {
            "Host": "api.passport.pptv.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/30"
        self.name = "PPTV"
        self.website = "http://www.pptv.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        PPTV聚力-始终和你同一频道,汇聚最清晰,最流畅的网络各类最新热门直播、点播视频。
        '''

        self.cellphoneUrl = "http://api.passport.pptv.com/checkRegister"
        self.emailUrl = ""
        self.usernameUrl = "http://api.passport.pptv.com/v3/query/loginname_exist.do?logintype=username"

    def verifyCellphone(self):
        data = {"loginid": self.content, "sceneFlag": "1", "channel":"208000103005", "format": "jsonp"}
        resp = requests.get(self.cellphoneUrl, headers=headers, params=data)
        try:
            res = json.loads(resp.text[5:-1])
        except:
            return False
        if res["errorCode"] == 6:
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"username": self.content}
        resp = requests.get(self.usernameUrl, headers=headers, params=data)
        if "<errorCode>5</errorCode>" in resp.text:
            return True
        else:
            return False
