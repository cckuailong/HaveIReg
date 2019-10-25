import requests, re, warnings

warnings.filterwarnings("ignore")


class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/28"
        self.name = "前程无忧"
        self.website = "http://www.51job.com/"
        self.category = "JOB"
        self.iconUrl = ""
        self.desc = '''
        前程无忧是国内第一个集多种媒介资源优势的专业人力资源服务机构。
        '''

        self.cellphoneUrl = "https://login.51job.com/ajax/checkinfo.php"
        self.emailUrl = "https://login.51job.com/ajax/checkinfo.php"
        self.usernameUrl = ""

    def verifyCellphone(self):
        data = {"value": self.content, "nation":"CN", "type":"mobile"}
        resp = requests.get(self.cellphoneUrl, params=data, verify=False)
        if "\"result\":1" in resp.text:
            return True
        else:
            return False

    def verifyEmail(self):
        data = {"value": self.content, "type": "useremail"}
        resp = requests.get(self.emailUrl, params=data, verify=False)
        if "\"result\":1" in resp.text:
            return True
        else:
            return False

    def verifyUsername(self):
        return False
