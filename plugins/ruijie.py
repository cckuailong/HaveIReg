import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "锐捷网络"
        self.website = "https://ruijie.zhiye.com"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        锐捷网络以“场景创新”在竞争激烈的网络设备市场开辟出独树一帜的发展大道。
        '''

        self.cellphoneUrl = "https://ruijie.zhiye.com/User/Account/CheckPhoneOccupied"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"mobile": self.content, "businessType": 1}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["Message"] == "registered":
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
