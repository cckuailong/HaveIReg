import requests, re, warnings

warnings.filterwarnings("ignore")

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "好乐买"
        self.website = "http://www.okbuy.com/"
        self.category = "EC"
        self.iconUrl = ""
        self.desc = '''
        好乐买使用OkBuy的用意就是让更多的人体验到便捷的网上购物体验，好，就来买吧！
        '''

        self.cellphoneUrl = "http://www.okbuy.com/ajax/tel/check_bind"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"tel": self.content}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        if resp.text == "0":
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
