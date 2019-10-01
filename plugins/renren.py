import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/30"
        self.name = "人人网"
        self.website = "http://www.renren.com"
        self.category = "SC"
        self.iconUrl = ""
        self.desc = '''
        人人网 校内是一个真实的社交网络，联络你和你周围的朋友。 加入人人网校内你可以:联络朋友，了解他们的最新动态；和朋友分享相片、音乐和电影；找到老同学，结识新朋友；用照片和日志记录生活,展示自我。
        '''

        self.cellphoneUrl = "http://reg.renren.com/AjaxRegisterAuth.do"
        self.emailUrl = "http://reg.renren.com/AjaxRegisterAuth.do"
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {
            "authType": "email",
            "stage":3,
            "value":self.content,
        }
        resp = requests.post(self.cellphoneUrl, data=data)
        if "不能注册" in resp.text:
            return True
        else:
            return False

    def verifyEmail(self):
        data = {
            "authType": "email",
            "stage":2,
            "value":self.content,
        }
        resp = requests.post(self.emailUrl, data=data)
        if "帐号已存在" in resp.text:
            return True
        else:
            return False

    def verifyUsername(self):
        return False
