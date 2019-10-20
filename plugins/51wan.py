import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/20"
        self.name = "51wan"
        self.website = "http://51wan.com"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        51wan致力于成为全球领先的互联网快乐服务商，本着“让互联网快乐起来”的理念，依托“速度运营”“敏锐研发”“娱乐平台”三大核心竞争力、致力于打造以游戏娱乐为主的在线娱乐品牌网站。
        '''

        self.cellphoneUrl = "http://passport.51wan.com/reg_index_check_0.html"
        self.emailUrl = "http://passport.51wan.com/reg_index_check_0.html"
        self.usernameUrl = "http://passport.51wan.com/reg_index_check_0.html"

    def verifyCellphone(self):
        data = {"type": "username", "username": self.content}
        resp = requests.get(self.cellphoneUrl, params=data)
        if resp.text == "false":
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"type": "username", "username": self.content}
        resp = requests.get(self.emailUrl, params=data)
        if resp.text == "false":
            return True
        else:
            return False

    def verifyUsername(self):
        data = {"type": "username", "username": self.content}
        resp = requests.get(self.usernameUrl, params=data)
        if resp.text == "false":
            return True
        else:
            return False
