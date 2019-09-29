import requests, re, warnings
import json
warnings.filterwarnings("ignore")

headers = {
            "Host": "account.iiyi.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://account.iiyi.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://account.iiyi.com/register?referer=https%3A%2F%2Fwww.iiyi.com%2F",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "爱爱医"
        self.website = "https://www.iiyi.com/"
        self.category = "HOSP"
        self.iconUrl = ""
        self.desc = '''
        爱爱医是面向医务人员的医学、药学专业知识与经验交流平台，并为医生提供国家医学考试中心信息服务的专业医学网站
        '''

        self.cellphoneUrl = "https://account.iiyi.com/index/checkbind"
        self.emailUrl = ""
        self.usernameUrl = "https://account.iiyi.com/index/checkuser"

    def verifyCellphone(self):
        data = {"bind": self.content}
        resp = requests.post(self.cellphoneUrl, headers=headers, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == 400:
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"username": self.content}
        resp = requests.post(self.usernameUrl, headers=headers, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["code"] == 400:
            return True
        else:
            return False


testReg = TestReg("15846007766")
testReg.verifyCellphone()