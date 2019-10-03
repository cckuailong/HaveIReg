import requests, re, warnings
import json
warnings.filterwarnings("ignore")
headers = {
            "Host": "www.nowcoder.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Referer": "https://www.nowcoder.com/register",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie":"NOWCODERUID=42C96151760CE2038E3BB22B36E42FD0; NOWCODERCLINETID=111971556C59C2A688972F0E1CFEDB0E; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1569971169,1570108683; callBack=; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1570109602; SERVERID=11b18158070cf9d7800d51a2f8a74633|1570109602|1570108681"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/03"
        self.name = ""
        self.website = ""
        self.category = ""
        self.iconUrl = ""
        self.desc = '''

        '''

        self.cellphoneUrl = "https://www.nowcoder.com/nccommon/register/check-phone-available?phone=%2B8615846007766"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"phone": "%2B86"+self.content}
        resp = requests.get(self.cellphoneUrl, headers=headers, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == 1:
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
