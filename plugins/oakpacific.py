import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/03"
        self.name = "千橡游戏"
        self.website = "http://www.imop.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        千橡游戏隶属于国内首家独立研发并运营网页游戏的千橡互动集团。
        '''

        self.cellphoneUrl = ""
        self.emailUrl = ""
        self.usernameUrl = "http://gc.imop.com/passport/check.php"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        data = {"game_username": self.content}
        resp = requests.post(self.usernameUrl, data=data)
        if resp == "0":
            return True
        else:
            return False
