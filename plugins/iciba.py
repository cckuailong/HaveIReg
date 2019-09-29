import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/29"
        self.name = "金山词霸"
        self.website = "http://www.iciba.com/"
        self.category = "EDU"
        self.iconUrl = ""
        self.desc = '''
        爱词霸英语为广大网友提供在线翻译、在线词典、英语口语、英语学习资料、汉语词典,金山词霸下载等服务
        '''

        self.cellphoneUrl = ""
        self.emailUrl = "http://my.iciba.com/?c=register&m=checkEmail"
        self.usernameUrl = ""

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        data = {"e": self.content}
        resp = requests.post(self.emailUrl, data=data)
        if resp.text == "0":
            return False
        else:
            return True

    def verifyUsername(self):
        return False


testReg = TestReg("346813862@qq.com")
print(testReg.verifyEmail())