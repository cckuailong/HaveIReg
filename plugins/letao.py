import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "乐淘网"
        self.website = "https://new.letao.com/"
        self.category = "EC"
        self.iconUrl = ""
        self.desc = '''
        乐淘网是中国主要的运动鞋、皮鞋网络零售网站，聚焦在垂直的鞋及其相关商品领域深耕。
        '''

        self.cellphoneUrl = "http://www.letao.com/ff80808157ffc1c2015800534d4c0000/checkPhone.do"
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"phone": self.content}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        if resp.text == "true":
            return True
        else:
            return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False
