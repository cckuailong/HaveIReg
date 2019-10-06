import requests, re, warnings
import json
warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/10/06"
        self.name = "去哪儿网"
        self.website = "https://www.qunar.com/"
        self.category = "ENT"
        self.iconUrl = ""
        self.desc = '''
        去哪儿是中国领先的旅游搜索引擎，去哪儿是目前全球最大的中文在线旅行网站。
        '''

        self.cellphoneUrl = "https://user.qunar.com/ajax/validator.jsp"
        self.emailUrl = "https://user.qunar.com/ajax/validator.jsp"
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"method":self.content , "prenum": "86"}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["errCode"] == 11009:
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"method": self.content}
        resp = requests.post(self.cellphoneUrl, data=data, verify=False)
        try:
            res = json.loads(resp.text)
        except:
            return False
        if res["errCode"] == 11009:
            return True
        else:
            return False

    def verifyUsername(self):
        return False
