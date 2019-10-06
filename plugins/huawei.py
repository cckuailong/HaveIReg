import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "华为"
        self.website = "http://career.huawei.com"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        华为技术有限公司是一家生产销售通信设备的民营通信科技公司。
        '''

        self.cellphoneUrl = "https://uniportal.huawei.com/accounts/register.do?method=checkIsVerifiedPhone"
        self.emailUrl = "https://uniportal.huawei.com/accounts/register.do?method=checkEmail"
        self.usernameUrl = "https://uniportal.huawei.com/accounts/register.do?method=checkAccount"

    def verifyCellphone(self):
        data = {"telephoneNumber": "%2B86%20"+self.content, "method": "checkIsVerifiedPhone"}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        if resp.text == "1":
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"email": self.content, "method": "checkEmail"}
        resp = requests.post(self.emailUrl, data=data, verify=False)
        if resp.text == "1":
            return True
        else:
            return False

    def verifyUsername(self):
        data = {"user_id": self.content, "method":"checkAccount"}
        resp = requests.post(self.usernameUrl, data=data, verify=False)
        if resp.text == "1":
            return True
        else:
            return False
